from flask import Blueprint, url_for, redirect

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("", methods=["GET"])
def index():
    return redirect(url_for("users.login_user"))
