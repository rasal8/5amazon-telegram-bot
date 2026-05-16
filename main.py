import asyncio
import os

from amazon_paapi import AmazonApi
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "8843677021:AAEFr8bnX6szlIcvXV4gFs5OCt9CceBx1fQ"
CHAT_ID = "-1003615762835"

ACCESS_KEY = os.getenv("AMAZON_ACCESS_KEY")
SECRET_KEY = os.getenv("AMAZON_SECRET_KEY")
PARTNER_TAG = PARTNER_TAG = "rrasal-21"

amazon = AmazonApi(
    ACCESS_KEY,
    SECRET_KEY,
    PARTNER_TAG,
    "IN"
)

categories = {
    "🏠 Home Decor": "home decor aesthetic",
    "👗 Korean Outfits": "korean fashion women",
    "✨ Korean Products": "korean aesthetic products",
    "💍 Jewellery": "minimal jewellery women"
}


async def send_products():

    bot = Bot(token=BOT_TOKEN)

    for category, keyword in categories.items():

        try:

            products = amazon.search_items(
                keywords=keyword,
                search_index="All",
                item_count=5
            )

            message = f"📌 {category}\n\n"

            keyboard = []

            for index, product in enumerate(products, start=1):

                try:

                    title = product.title[:60]

                    price = (
                        product.prices.price
                        if product.prices
                        else "N/A"
                    )

                    link = product.detail_page_url

                    tag = (
                        "🔥 Trending"
                        if index <= 3
                        else "🌱 Evergreen"
                    )

                    message += (
                        f"{index}. {title}\n"
                        f"{tag}\n"
                        f"💰 ₹{price}\n\n"
                    )

                    keyboard.append([
                        InlineKeyboardButton(
                            f"🛒 View Product {index}",
                            url=link
                        )
                    ])

                except:
                    continue

            reply_markup = InlineKeyboardMarkup(keyboard)

            await bot.send_message(
                chat_id=CHAT_ID,
                text=message[:4000],
                reply_markup=reply_markup
            )

        except Exception as e:

            await bot.send_message(
                chat_id=CHAT_ID,
                text=f"❌ Error in {category}\n\n{e}"
            )


asyncio.run(send_products())
