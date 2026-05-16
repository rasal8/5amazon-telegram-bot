import os
import asyncio
from telegram import Bot

BOT_TOKEN = "8843677021:AAEFr8bnX6szlIcvXV4gFs5OCt9CceBx1fQ"
CHAT_ID = "-1003615762835"

ACCESS_KEY = os.getenv("AMAZON_ACCESS_KEY")
SECRET_KEY = os.getenv("AMAZON_SECRET_KEY")
PARTNER_TAG = os.getenv("AMAZON_PARTNER_TAG")


async def send_message():

    bot = Bot(token=BOT_TOKEN)

    text = (
        "✅ Amazon API Connected Successfully\n\n"
        f"Partner Tag: {PARTNER_TAG}"
    )

    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )


asyncio.run(send_message())
