"""
Run this ONCE to authenticate Telethon on the server.
After this, main.py can run unattended.

Usage: python auth.py
"""
import asyncio
import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()


async def authenticate():
    api_id = int(os.environ["TELEGRAM_API_ID"])
    api_hash = os.environ["TELEGRAM_API_HASH"]
    phone = os.environ["TELEGRAM_PHONE"]

    client = TelegramClient("telegram_session", api_id, api_hash)
    await client.start(phone=phone)

    me = await client.get_me()
    print(f"Authenticated as: {me.first_name} (@{me.username})")
    print(f"Your Telegram user ID (use as YOUR_CHAT_ID): {me.id}")
    print("Session saved to telegram_session.session — keep this file safe.")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(authenticate())
