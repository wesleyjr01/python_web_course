from typing import Dict, List
from models.item import Item
from models.model import Model


class Alert(Model):

    collection = "alerts"

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        super().__init__(_id)
        self.item_id = item_id
        self.price_limit = price_limit
        self.item = Item.find_by_id(self.item_id)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
        }

    def load_item_price(self) -> float:
        return self.item.load_price()

    def notify_if_price_reached(self) -> None:
        if self.item.price <= self.price_limit:
            print(
                f"Item {self.item} has reached a price under {self.price_limit}.\nLatest price: {self.item.price}"
            )
