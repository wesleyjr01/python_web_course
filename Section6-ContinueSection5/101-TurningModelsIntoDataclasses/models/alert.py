from dataclasses import dataclass, field
from typing import Dict
from models.item import Item
from models.model import Model
import uuid


@dataclass(eq=False)
class Alert(Model):

    collection: str = field(init=False, default="alerts")
    item_id: str
    price_limit: float
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
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
