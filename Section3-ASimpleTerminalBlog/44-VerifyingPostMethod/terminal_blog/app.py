from models.post import Post
from database import Database

Database.initialize()

# post = Post(
#     blog_id="123",
#     title="Another good posterino, once more",
#     content="rçrçrçrçrrç",
#     author="Salgadao",
# )

# post.save_to_mongo()

post1 = Post.from_mongo("1961c84e000d4cba8504225bca7c2473")
print(post1)

post2 = Post.from_blog("123")
print(post2)
