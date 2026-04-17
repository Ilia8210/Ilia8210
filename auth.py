"""
Run this ONCE in Google Colab to get your Telegram session string.

In Colab:
1. !pip install telethon
2. Copy-paste this entire file and run it
3. Enter your phone number and the code from Telegram
4. Copy the printed session string
5. Add it as TELEGRAM_SESSION in Railway Variables
"""
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(input("Enter API_ID: "))
API_HASH = input("Enter API_HASH: ")
PHONE = input("Enter phone (e.g. +79001234567): ")


async def get_session():
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.start(phone=PHONE)
    me = await client.get_me()
    print(f"\nAuthenticated as: {me.first_name} (@{me.username})")
    print(f"\nYour TELEGRAM_SESSION string (copy this to Railway Variables):")
    print(client.session.save())
    await client.disconnect()


asyncio.run(get_session())
