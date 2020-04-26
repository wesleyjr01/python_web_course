import requests
from bs4 import BeautifulSoup

request = requests.get(
    "https://www.johnlewis.com/philippe-starck-for-kartell-masters-chair/black/p326288"
)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
# .stip() to remove white spaces
print(f"Price Parsed: {element.text.strip()}")
