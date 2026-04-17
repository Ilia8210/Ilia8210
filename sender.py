import os
import asyncio
from datetime import datetime

from telegram import Bot


async def _send(pdf_path: str):
    token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["YOUR_CHAT_ID"]

    bot = Bot(token=token)
    date_str = datetime.now().strftime("%Y-%m-%d")

    async with bot:
        with open(pdf_path, "rb") as f:
            await bot.send_document(
                chat_id=chat_id,
                document=f,
                filename=f"ux_report_{date_str}.pdf",
                caption=f"UX Feedback Report — {date_str}",
            )


def send_pdf(pdf_path: str):
    asyncio.run(_send(pdf_path))
