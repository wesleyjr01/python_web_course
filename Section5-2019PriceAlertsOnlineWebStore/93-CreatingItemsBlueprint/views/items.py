""" This file is going to contain our item's blueprint
that will contain all the endpoints related to items."""

import json
from flask import Blueprint, render_template, request
from models.item import Item

item_blueprint = Blueprint("items", __name__)


@item_blueprint.route("/")
def index():
    items = Item.find_all()
    return render_template("items/index.html", items=items)


@item_blueprint.route("/new", methods=["GET", "POST"])
def new_item():
    """ we are accessing fields names inside requests.form"""
    if request.method == "POST":
        url = request.form["url"]
        tag_name = request.form["tag_name"]
        query = json.loads(request.form["query"])

        Item(url, tag_name, query).save_to_mongo()

    return render_template("items/new_item.html")
