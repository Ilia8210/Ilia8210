import os
import base64
from datetime import datetime, timedelta, timezone
from io import BytesIO

from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from PIL import Image

SESSION_FILE = "telegram_session"
MAX_MESSAGES = 300
MAX_IMAGES = 10
IMAGE_MAX_PX = 1024


def _is_image(msg) -> bool:
    if isinstance(msg.media, MessageMediaPhoto):
        return True
    if isinstance(msg.media, MessageMediaDocument):
        mime = getattr(msg.media.document, "mime_type", "")
        return mime.startswith("image/")
    return False


def _compress_image(raw: bytes) -> tuple[bytes, str]:
    img = Image.open(BytesIO(raw))
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    if max(img.size) > IMAGE_MAX_PX:
        ratio = IMAGE_MAX_PX / max(img.size)
        img = img.resize(
            (int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS
        )
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=82)
    return buf.getvalue(), "image/jpeg"


async def fetch_channel_data(channel: str, hours: int = 24) -> dict:
    api_id = int(os.environ["TELEGRAM_API_ID"])
    api_hash = os.environ["TELEGRAM_API_HASH"]
    since = datetime.now(timezone.utc) - timedelta(hours=hours)

    texts = []
    images = []

    client = TelegramClient(SESSION_FILE, api_id, api_hash)
    async with client:
        entity = await client.get_entity(channel)

        async for msg in client.iter_messages(entity, limit=MAX_MESSAGES):
            msg_date = msg.date
            if msg_date.tzinfo is None:
                msg_date = msg_date.replace(tzinfo=timezone.utc)
            if msg_date < since:
                break

            if msg.text and msg.text.strip():
                texts.append(
                    {"id": msg.id, "text": msg.text.strip(), "date": msg_date.isoformat()}
                )

            if _is_image(msg) and len(images) < MAX_IMAGES:
                try:
                    buf = BytesIO()
                    await client.download_media(msg, file=buf)
                    raw, mime = _compress_image(buf.getvalue())
                    images.append(
                        {
                            "message_id": msg.id,
                            "data": base64.b64encode(raw).decode(),
                            "media_type": mime,
                            "date": msg_date.isoformat(),
                        }
                    )
                except Exception:
                    pass

    return {"texts": texts, "images": images}
