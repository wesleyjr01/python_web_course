from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(title="another blog", author="Salgadao", description="Some description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.blog_id).json()

# Se usar o mesmo blog_id,  as duas retornam a mesma coisa
print(f"blog.get_posts() : {blog.get_posts()}")
print(f"\nBlog.from_mongo(blog.blog_id).json() : {from_database}")
