from database import Database
from models.blog import Blog


class Menu:
    def __init__(self):
        self.user = input("Enter you author name: ")
        self.user_blog = None
        if self._user_has_account():
            print(f"Welcome back {self.user}")
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one("blogs", {"author": self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to Read (R) or Write (W) blogs?")
        if read_or_write == "R":
            pass
        elif read_or_write == "W":
            pass
        else:
            print("Thank you for blogging!")
