async def send_products():

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Bot working perfectly"
    )

asyncio.run(send_products())
