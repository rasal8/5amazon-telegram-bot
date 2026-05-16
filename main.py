import asyncio
import random
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = "8843677021:AAEFr8bnX6szlIcvXV4gFs5OCt9CceBx1fQ"
CHAT_ID = "-1003615762835"

products = {
    "🏠 Home Decor": [

        {
            "title": "Aesthetic Bedside Lamp",
            "price": "799",
            "link": "https://www.amazon.in/s?k=bedside+lamp&tag=rrasal-21"
        },

        {
            "title": "Minimal Beige Room Decor",
            "price": "599",
            "link": "https://www.amazon.in/s?k=beige+room+decor&tag=rrasal-21"
        },

        {
            "title": "Cozy Desk Setup Light",
            "price": "999",
            "link": "https://www.amazon.in/s?k=desk+setup+light&tag=rrasal-21"
        },

        {
            "title": "Korean Style Wall Decor",
            "price": "699",
            "link": "https://www.amazon.in/s?k=korean+wall+decor&tag=rrasal-21"
        },

        {
            "title": "Modern Table Decor",
            "price": "499",
            "link": "https://www.amazon.in/s?k=table+decor&tag=rrasal-21"
        }
    ],

    "👗 Korean Outfits": [

        {
            "title": "Oversized Korean T-Shirt",
            "price": "499",
            "link": "https://www.amazon.in/s?k=oversized+korean+tshirt+women&tag=rrasal-21"
        },

        {
            "title": "Korean Casual Shirt",
            "price": "699",
            "link": "https://www.amazon.in/s?k=korean+shirt+women&tag=rrasal-21"
        },

        {
            "title": "Wide Leg Korean Jeans",
            "price": "999",
            "link": "https://www.amazon.in/s?k=wide+leg+korean+jeans&tag=rrasal-21"
        },

        {
            "title": "Pinterest Korean Hoodie",
            "price": "899",
            "link": "https://www.amazon.in/s?k=korean+hoodie+women&tag=rrasal-21"
        },

        {
            "title": "Korean Aesthetic Top",
            "price": "599",
            "link": "https://www.amazon.in/s?k=korean+top+women&tag=rrasal-21"
        }
    ],

    "✨ Korean Products": [

        {
            "title": "Cute Desk Accessories",
            "price": "399",
            "link": "https://www.amazon.in/s?k=cute+desk+accessories&tag=rrasal-21"
        },

        {
            "title": "Aesthetic Study Setup",
            "price": "799",
            "link": "https://www.amazon.in/s?k=study+setup+aesthetic&tag=rrasal-21"
        },

        {
            "title": "Korean Stationery Set",
            "price": "299",
            "link": "https://www.amazon.in/s?k=korean+stationery&tag=rrasal-21"
        },

        {
            "title": "Cute Phone Accessories",
            "price": "499",
            "link": "https://www.amazon.in/s?k=phone+accessories+aesthetic&tag=rrasal-21"
        },

        {
            "title": "Korean Desk Organizer",
            "price": "599",
            "link": "https://www.amazon.in/s?k=korean+desk+organizer&tag=rrasal-21"
        }
    ],

    "💍 Jewellery": [

        {
            "title": "Minimal Pearl Necklace",
            "price": "299",
            "link": "https://www.amazon.in/s?k=pearl+necklace&tag=rrasal-21"
        },

        {
            "title": "Korean Earrings",
            "price": "249",
            "link": "https://www.amazon.in/s?k=korean+earrings&tag=rrasal-21"
        },

        {
            "title": "Minimal Gold Bracelet",
            "price": "399",
            "link": "https://www.amazon.in/s?k=minimal+bracelet&tag=rrasal-21"
        },

        {
            "title": "Pinterest Aesthetic Ring",
            "price": "199",
            "link": "https://www.amazon.in/s?k=aesthetic+ring&tag=rrasal-21"
        },

        {
            "title": "Layered Necklace Set",
            "price": "499",
            "link": "https://www.amazon.in/s?k=layered+necklace&tag=rrasal-21"
        }
    ]
}


async def send_products():

    bot = Bot(token=BOT_TOKEN)

    for category, items in products.items():

        random.shuffle(items)

        trending = items[:3]
        evergreen = items[3:5]

        final_products = trending + evergreen

        message = f"📌 {category}\n\n"

        keyboard = []

        for index, product in enumerate(final_products, start=1):

            tag = (
                "🔥 Trending"
                if index <= 3
                else "🌱 Evergreen"
            )

            message += (
                f"{index}. {product['title']}\n"
                f"{tag}\n"
                f"💰 ₹{product['price']}\n\n"
            )

            keyboard.append([
                InlineKeyboardButton(
                    f"🛒 View Product {index}",
                    url=product["link"]
                )
            ])

        reply_markup = InlineKeyboardMarkup(keyboard)

        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            reply_markup=reply_markup
        )


asyncio.run(send_products())
