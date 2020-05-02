from common.database import Database
from models.item import Item
from models.model import Model
from typing import Dict, List
from uuid import uuid4


class Alert(Model):

    collection = "alerts"

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        self.item_id = item_id
        self.item = Item.get_by_id(self.item_id)
        self.price_limit = price_limit
        self._id = _id or uuid4().hex

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
        }

    def save_to_mongo(self) -> None:
        Database.insert(collection=Alert.collection, data=self.json())

    def load_item_price(self) -> float:
        return self.item.load_price()

    def notify_if_price_reached(self) -> None:
        if self.item.price <= self.price_limit:
            print(
                f"Item {self.item} has reached a price under {self.price_limit}.\nLatest price: {self.item.price}"
            )

    @classmethod
    def get_all(cls) -> List:
        alerts_from_db = Database.find(collection=cls.collection, query={})
        if alerts_from_db:
            return [cls(**alert) for alert in alerts_from_db]
