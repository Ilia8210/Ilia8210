import asyncio
import os
import sys
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

from fetcher import fetch_channel_data
from analyzer import analyze_feedback
from report import generate_report
from sender import send_pdf


def log(msg: str):
    print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)


def main():
    channel = os.environ.get("TELEGRAM_CHANNEL")
    if not channel:
        print("Error: TELEGRAM_CHANNEL not set in .env")
        sys.exit(1)

    log(f"Fetching messages from {channel}...")
    data = asyncio.run(fetch_channel_data(channel))

    n_texts = len(data["texts"])
    n_images = len(data["images"])
    log(f"Found {n_texts} messages, {n_images} images")

    if n_texts == 0 and n_images == 0:
        log("No new messages in the last 24 hours. Skipping.")
        return

    log("Analyzing feedback with Claude...")
    analysis = analyze_feedback(data)

    if "error" in analysis:
        log(f"Analysis error: {analysis['error']}")
        sys.exit(1)

    date_str = datetime.now().strftime("%Y-%m-%d")
    pdf_path = f"ux_report_{date_str}.pdf"

    log("Generating PDF report...")
    generate_report(analysis, pdf_path)

    log("Sending report to Telegram...")
    send_pdf(pdf_path)

    log(f"Done. Report sent: {pdf_path}")


if __name__ == "__main__":
    main()
