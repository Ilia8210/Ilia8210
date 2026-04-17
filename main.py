import os
import sys
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

from fetcher import fetch_channel_data
from analyzer import analyze_feedback
from report import generate_report


def log(msg: str):
    print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)


def main():
    channel = os.environ.get("TELEGRAM_CHANNEL", "@catapult_community")

    log(f"Fetching messages from {channel}...")
    data = fetch_channel_data(channel)

    n = len(data["texts"])
    log(f"Found {n} messages")

    if n == 0:
        log("No messages found. Check that the channel username is correct and public.")
        sys.exit(1)

    log("Analyzing with Claude...")
    analysis = analyze_feedback(data)

    if "error" in analysis:
        log(f"Error: {analysis['error']}")
        sys.exit(1)

    date_str = datetime.now().strftime("%Y-%m-%d")
    pdf_path = f"ux_report_{date_str}.pdf"

    log("Generating PDF...")
    generate_report(analysis, pdf_path)

    log(f"Done! Report saved: {pdf_path}")


if __name__ == "__main__":
    main()
