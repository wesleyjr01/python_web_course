import re
import requests
from bs4 import BeautifulSoup


class Item:
    def __init__(self, url, tag_name, query):
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None

    def load_price(self):
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"((\d{1,3},)?\d*(\.|,)\d{1,2})")
        match = pattern.search(string_price)
        string_price = match.group(1)
        without_commas = string_price.replace(",", "")
        self.price = float(without_commas)
        return self.price
