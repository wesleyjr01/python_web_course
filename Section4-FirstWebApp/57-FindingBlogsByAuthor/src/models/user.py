from common.database import Database
from models.blog import Blog
import uuid
from werkzeug.security import safe_str_cmp
from flask import session


class User:
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        """ Its not safe to send this over the network """
        return {"email": self.email, "_id": self._id, "password": self.password}

    @classmethod
    def get_by_email(cls, email):
        user = Database.find_one(collection="users", query={"email": email})
        if user:
            return cls(**user)
        return None

    @classmethod
    def get_by_id(cls, _id):
        user = Database.find_one(collection="users", query={"_id": _id})
        if user:
            return cls(**user)
        return None

    @staticmethod
    def login_valid(email, password):
        # Check whether a user's email matches the password they sent us
        user = User.get_by_email(email)
        if user and safe_str_cmp(user.password, password):
            return True
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session["email"] = email
            return True
        else:
            return False

    @staticmethod
    def login(user_email):
        # Login_valid has already been called
        session["email"] = user_email

    @staticmethod
    def logout():
        session["email"] = None

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def save_to_mongo(self):
        Database.insert(collection="users", data=self.json())
