"""
In Python, the "and" returns the first value if it evaluates to false,
 otherwise it returns the second value.
The "or" operator returns the first value if it evaluates to true,
 otherwise it returns the second value.
"""
from typing import Dict, List
import re
import uuid
import requests
from bs4 import BeautifulSoup
from common.database import Database
from models.model import Model


class Item(Model):

    collection = "items"

    def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None):
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        return f"<Item {self.url}>"

    def load_price(self) -> float:
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

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query,
        }

    def save_to_mongo(self) -> None:
        Database.insert(Item.collection, self.json())

    @classmethod
    def get_all(cls) -> List:
        items_from_db = Database.find(collection=cls.collection, query={})
        if items_from_db:
            return [cls(**item) for item in items_from_db]

    @classmethod
    def get_by_id(cls, item_id) -> "Item":
        item = Database.find_one(collection=cls.collection, query={"_id": item_id})
        if item:
            return cls(**item)
