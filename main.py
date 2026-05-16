import os

ACCESS_KEY = os.getenv("AMAZON_ACCESS_KEY")
SECRET_KEY = os.getenv("AMAZON_SECRET_KEY")
PARTNER_TAG = os.getenv("AMAZON_PARTNER_TAG")

print("Amazon API Connected Successfully")
print(ACCESS_KEY)
print(PARTNER_TAG)
