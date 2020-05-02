from typing import List, TypeVar, Type, Dict
import uuid
from abc import ABCMeta, abstractmethod
from common.database import Database

T = TypeVar("T", bound="Model")


class Model(metaclass=ABCMeta):
    """ Superclass of all models defined """

    collection: str

    def __init__(self, _id: str = None):
        self._id = _id or uuid.uuid4().hex

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    def save_to_mongo(self):
        """ Database.update is going to inser a new thing, unless
        there is already something in the database matching this <_id>.
        After running {"_id": self._id}, if something comes back, we are going
        to update that thing instead of inserting a new one. That's called upserting."""

        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    @classmethod
    def find_by_id(cls: Type[T], _id: str) -> T:
        element = cls.find_one_by("_id", _id)
        if element:
            return cls(**element)

    @classmethod
    def find_all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.find(collection=cls.collection, query={})
        if elements_from_db:
            return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: str) -> T:
        element = Database.find_one(cls.collection, {attribute: value})
        if element:
            return cls(**element)

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:
        elements = Database.find(cls.collection, {attribute: value})
        if elements:
            return [cls(**elem) for elem in elements]
