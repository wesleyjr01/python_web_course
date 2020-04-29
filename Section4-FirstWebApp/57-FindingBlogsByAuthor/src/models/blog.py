import uuid
from models.post import Post
import datetime
from common.database import Database


class Blog:
    def __init__(self, author, title, description, author_id, _id=None, **kwargs):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, created_date=datetime.datetime.utcnow()):
        """ add a new post to mongo, from blog(id=_id) """
        post = Post(
            blog_id=self._id,
            title=title,
            content=content,
            author=self.author,
            created_date=created_date,
        )
        post.save_to_mongo()

    def get_posts(self):
        """ get posts from current blog(id=_id) """
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        """ save current blog(id=_id) information to mongo """
        Database.insert(collection="blogs", data=self.json())

    def json(self):
        """ retrieve info in JSON format from blog(id=_id) """
        return {
            "author": self.author,
            "author_id": self.author_id,
            "title": self.title,
            "description": self.description,
            "_id": self._id,
        }

    @classmethod
    def from_mongo(cls, _id):
        """ returns a Blog object with id _id"""
        blog_data = Database.find_one(collection="blogs", query={"_id": _id})

        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find_one(collection="blogs", query={"author_id": author_id})

        return [cls(**blog) for blog in blogs]
