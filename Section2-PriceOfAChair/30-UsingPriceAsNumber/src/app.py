import requests
from bs4 import BeautifulSoup

request = requests.get(
    "https://www.johnlewis.com/philippe-starck-for-kartell-masters-chair/black/p326288"
)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip()  # £177.00
price_without_symbol = string_price[1:]
# .stip() to remove white spaces
print(f"Price Parsed: {float(price_without_symbol)}")
