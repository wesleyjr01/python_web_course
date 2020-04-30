from flask import Flask, render_template, request, session, make_response
from models.user import User
from common.database import Database
from models.blog import Blog

app = Flask(__name__)
app.secret_key = "salgado"


@app.route("/")
def home_template():
    return render_template("home.html")


@app.route("/login")  # www.mysite.com/api/
def login_template():
    return render_template("login.html")


@app.route("/register")  # www.mysite.com/api/
def register_template():
    return render_template("register.html")


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route("/auth/login", methods=["POST"])
def login_user():
    email = request.form["email"]
    password = request.form["password"]

    if User.login_valid(email, password):
        User.login(email)
    else:
        session["email"] = None

    return render_template("profile.html", email=session["email"])


@app.route("/auth/register", methods=["POST"])
def register_user():
    email = request.form["email"]
    password = request.form["password"]

    user = User.register(email, password)
    if not user:
        session["email"] = "User Already Registered"

    return render_template("profile.html", email=session["email"])


@app.route("/blogs/new", methods=["POST", "GET"])
def create_new_blogs():
    if request.method == "GET":
        return render_template("new_blog.html")
    else:
        title = request.form["title"]
        description = request.form["description"]
        user = User.get_by_email(session["email"])

        new_blog = Blog(
            author=user.email, title=title, description=description, author_id=user._id
        )
        new_blog.save_to_mongo()

        return make_response(user_blogs(user._id))


@app.route("/blogs/<string:user_id>")
@app.route("/blogs")
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(_id=user_id)
    else:
        user = User.get_by_email(session["email"])
    blogs = user.get_blogs()
    return render_template("user_blogs.html", blogs=blogs, email=user.email)


@app.route("/posts/<string:blog_id>")
def blog_posts(blog_id):
    blog = Blog.from_mongo(_id=blog_id)
    posts = blog.get_posts()

    return render_template("posts.html", posts=posts, blog_title=blog.title)


if __name__ == "__main__":

    app.run(port=4555, debug=True)
