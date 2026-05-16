import requests
import random
import asyncio
from bs4 import BeautifulSoup
from telegram import Bot

BOT_TOKEN = "8843677021:AAEFr8bnX6szlIcvXV4gFs5OCt9CceBx1fQ"
CHAT_ID = "-1003615762835"

categories = {
    categories = {
    "🏠 Home Decor": "korean home decor aesthetic room decor lamp beige",
    
    "👗 Korean Outfits": "korean oversized fashion women aesthetic outfit",

    "✨ Korean Products": "korean aesthetic desk accessories cute products",

    "💍 Jewellery": "minimal korean pearl jewellery women"
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

            title = item.select_one("h2 span").text.strip()

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

    trending_products = products[:3]

    remaining_products = products[3:]

    if len(remaining_products) >= 2:
        evergreen_products = random.sample(remaining_products, 2)
    else:
        evergreen_products = remaining_products

    return trending_products + evergreen_products


async def send_products():

    bot = Bot(token=BOT_TOKEN)

    message = "📌 Daily Pinterest Product Feed\n\n"

    for category, search in categories.items():

        message += f"{category}\n\n"

        products = get_products(search)

        for index, product in enumerate(products, start=1):

            message += (
                f"{index}. {product['title']}\n"
                f"💰 ₹{product['price']}\n"
                f"🔗 {product['link']}\n\n"
            )

    await bot.send_message(chat_id=CHAT_ID, text=message[:4000])


asyncio.run(send_products())
