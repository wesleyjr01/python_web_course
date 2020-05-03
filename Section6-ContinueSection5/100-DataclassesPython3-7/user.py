import uuid
from typing import Dict
from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    password: str = field(repr=False)
    contry: str = field(default="United Kingdom")
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {"_id": self._id, "username": self.username}
