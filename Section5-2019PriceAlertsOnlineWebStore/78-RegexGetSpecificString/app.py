import re
import requests
from bs4 import BeautifulSoup

# URL = "https://www.johnlewis.com/2020-apple-ipad-pro-12-9-inch-a12z-bionic-ios-wi-fi-256gb/space-grey/p4949087"
URL = "https://www.johnlewis.com/sony-wh-xb900n-noise-cancelling-extra-bass-bluetooth-nfc-wireless-over-ear-headphones-with-mic-remote/black/p4221218"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}
response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

pattern = re.compile(r"((\d{1,3},)?\d*(\.|,)\d{1,2})")
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(",", "")
float_price = float(without_commas)
print(float_price)
