import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

MAX_PAGES = 15
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def fetch_channel_data(channel: str, hours: int = 24) -> dict:
    channel = channel.lstrip("@")
    base_url = f"https://t.me/s/{channel}"
    since = datetime.now(timezone.utc) - timedelta(hours=hours)

    texts = []
    before_id = None
    done = False

    for _ in range(MAX_PAGES):
        params = {"before": before_id} if before_id else {}
        resp = requests.get(base_url, params=params, headers=HEADERS, timeout=15)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")
        msg_divs = soup.select(".tgme_widget_message")

        if not msg_divs:
            break

        for msg in reversed(msg_divs):
            time_el = msg.select_one("time[datetime]")
            if not time_el:
                continue

            msg_date = datetime.fromisoformat(
                time_el["datetime"].replace("Z", "+00:00")
            )

            if msg_date < since:
                done = True
                break

            text_el = msg.select_one(".tgme_widget_message_text")
            if text_el:
                text = text_el.get_text(separator=" ").strip()
                if text:
                    texts.append({"text": text, "date": msg_date.isoformat()})

        if done:
            break

        oldest = msg_divs[0]
        post = oldest.get("data-post", "")
        if "/" in post:
            before_id = post.split("/")[-1]
        else:
            break

    return {"texts": texts, "images": []}
