from models.item import Item

URL = "https://www.johnlewis.com/2020-apple-ipad-pro-12-9-inch-a12z-bionic-ios-wi-fi-256gb/space-grey/p4949087"
# URL = "https://www.johnlewis.com/sony-wh-xb900n-noise-cancelling-extra-bass-bluetooth-nfc-wireless-over-ear-headphones-with-mic-remote/black/p4221218"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}

item = Item(URL, TAG_NAME, QUERY)
item.save_to_mongo()

print(item.load_price())
