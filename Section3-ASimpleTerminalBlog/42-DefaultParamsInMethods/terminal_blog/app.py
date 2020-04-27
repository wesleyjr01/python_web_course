from models.post import Post
from database import Database

Database.initialize()

kwargs = {"title": "first post", "content": "Awsome stuff", "author": "Wesley"}
post = Post(**kwargs)

print(post.content)
