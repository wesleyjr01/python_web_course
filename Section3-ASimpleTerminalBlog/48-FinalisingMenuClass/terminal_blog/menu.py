from database import Database
from models.blog import Blog


class Menu:
    def __init__(self):
        self.author = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print(f"Welcome back {self.author}")
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog_info = Database.find_one("blogs", {"author": self.author})
        if blog_info is not None:
            self.user_blog = Blog.from_mongo(blog_info["blog_id"])
            return True
        return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.author, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to Read (R) or Write (W) blogs?")
        if read_or_write == "R":
            self._list_blogs()
            self._view_blog()
        elif read_or_write == "W":
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection="blogs", query={})
        for blog in blogs:
            print(
                f"blog_id: {blog['blog_id']}, author: {blog['author']}, title: {blog['title']}, description: {blog['description']}"
            )

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog you want to read.")
        blog = Blog.from_mongo(blog_id=blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print(
                f"Date:{post['created_date']}, Title:{post['title']}, Content:{post['content']}, Author:{post['author']}\n"
            )
