import requests
import random
from bs4 import BeautifulSoup
from telegram import Bot

BOT_TOKEN = "8843677021:AAEFr8bnX6szlIcvXV4gFs5OCt9CceBx1fQ"
CHAT_ID = "8843677021"

bot = Bot(token=BOT_TOKEN)

categories = {
    "🏠 Home Decor": "cozy home decor aesthetic",
    "👗 Korean Outfits": "korean oversized fashion women",
    "✨ Korean Products": "korean aesthetic products",
    "💍 Jewellery": "minimal korean jewellery"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_products(search_query):

    url = f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}"

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

            image = item.select_one("img.s-image")["src"]

            products.append({
                "title": title,
                "price": price,
                "link": full_link,
                "image": image
            })

        except:
            continue

    trending_products = products[:3]

    remaining_products = products[3:]

    if len(remaining_products) >= 2:
        evergreen_products = random.sample(remaining_products, 2)
    else:
        evergreen_products = remaining_products

    final_products = trending_products + evergreen_products

    return final_products


message = "📌 Daily Pinterest Product Feed\n\n"

for category, search in categories.items():

    message += f"{category}\n\n"

    try:

        products = get_products(search)

        for index, product in enumerate(products, start=1):

            message += (
                f"{index}. {product['title']}\n"
                f"💰 ₹{product['price']}\n"
                f"🔗 {product['link']}\n\n"
            )

    except Exception as e:

        message += f"Error loading {category}\n\n"

bot.send_message(chat_id=CHAT_ID, text=message[:4000])

print("Products sent successfully")
