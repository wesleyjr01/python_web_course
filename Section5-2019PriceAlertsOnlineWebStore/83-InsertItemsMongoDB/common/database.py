""" URI stands for Uniform Resource Identifier """
from typing import Dict
import pymongo


class Database:
    """ the database is named pricing in our case """

    URI = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)
