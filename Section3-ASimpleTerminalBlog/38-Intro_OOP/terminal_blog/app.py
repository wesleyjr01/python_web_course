from models.post import Post

kwargs = {"title": "first post", "content": "Awsome stuff", "author": "Wesley"}
post = Post(**kwargs)

print(post.content)
