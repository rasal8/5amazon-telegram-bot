import asyncio
from telegram import Bot

BOT_TOKEN = "8843677021:AAEFr8bnX6szlIcvXV4gFs5OCt9CceBx1fQ"
CHAT_ID = "-1003615762835"

async def send_products():

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Bot working perfectly"
    )

asyncio.run(send_products())
