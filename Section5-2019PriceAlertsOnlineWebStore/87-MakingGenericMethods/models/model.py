from typing import List
from abc import ABCMeta, abstractmethod
from common.database import Database


class Model(metaclass=ABCMeta):
    @abstractmethod
    def json(self):
        raise NotImplementedError

    @classmethod
    def get_all(cls) -> List:
        elements_from_db = Database.find(collection=cls.collection, query={})
        if elements_from_db:
            return [cls(**elem) for elem in elements_from_db]
