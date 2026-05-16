import requests
import random
import asyncio
from bs4 import BeautifulSoup
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "8843677021:AAEFr8bnX6szlIcvXV4gFs5OCt9CceBx1fQ"
CHAT_ID = "-1003615762835"

categories = {
    "🏠 Home Decor": {
        "trending": "aesthetic bedside lamp",
        "evergreen": "minimal beige room decor"
    },

    "👗 Korean Outfits": {
        "trending": "korean oversized tshirt women",
        "evergreen": "korean casual outfit women"
    },

    "✨ Korean Products": {
        "trending": "cute aesthetic desk setup",
        "evergreen": "korean aesthetic accessories"
    },

    "💍 Jewellery": {
        "trending": "pearl jewellery women",
        "evergreen": "minimal necklace women"
    }
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


def get_products(search_query):

    url = f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}&ref=nb_sb_noss"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    items = soup.select("div.s-result-item")

    products = []

    for item in items:

        try:

            title = item.select_one("h2 span").text.strip()[:55]

            link = item.select_one("a.a-link-normal")["href"]

            full_link = "https://www.amazon.in" + link

            price_whole = item.select_one("span.a-price-whole")

            price = price_whole.text.strip() if price_whole else "N/A"

            products.append({
                "title": title,
                "price": price,
                "link": full_link
            })

        except:
            continue

    return products[:5]


async def send_products():

    bot = Bot(token=BOT_TOKEN)

    for category, searches in categories.items():

        message = f"📌 {category}\n\n"

        trending_products = get_products(searches["trending"])[:3]

        evergreen_products = get_products(searches["evergreen"])[:2]

        final_products = trending_products + evergreen_products

        keyboard = []

        for index, product in enumerate(final_products, start=1):

            product_type = "🔥 Trending" if index <= 3 else "🌱 Evergreen"

            message += (
                f"{index}. {product['title']}\n"
                f"{product_type}\n"
                f"💰 ₹{product['price']}\n\n"
            )

            keyboard.append(
                [
                    InlineKeyboardButton(
                        f"🛒 Product {index}",
                        url=product['link']
                    )
                ]
            )

        reply_markup = InlineKeyboardMarkup(keyboard)

        await bot.send_message(
            chat_id=CHAT_ID,
            text=message[:4000],
            reply_markup=reply_markup
        )


asyncio.run(send_products())
