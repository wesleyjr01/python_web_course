import uuid
from models.post import Post
import datetime
from database import Database


class Blog:
    def __init__(self, author, title, description, blog_id=None, **kwargs):
        self.author = author
        self.title = title
        self.description = description
        self.blog_id = uuid.uuid4().hex if blog_id is None else blog_id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        post = Post(
            blog_id=self.blog_id,
            title=title,
            content=content,
            author=self.author,
            date=datetime.datetime.utcnow(),
        )
        post.save_to_mongo()

    def get_posts(self):
        """get posts from blog"""
        return Post.from_blog(self.blog_id)

    def save_to_mongo(self):
        Database.insert(collection="blogs", data=self.json())

    def json(self):
        return {
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "blog_id": self.blog_id,
        }

    @classmethod
    def from_mongo(cls, blog_id):
        """ get blog """
        blog_data = Database.find_one(collection="blogs", query={"blog_id": blog_id})

        return cls(**blog_data)
