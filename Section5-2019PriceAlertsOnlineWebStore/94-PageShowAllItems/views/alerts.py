import json
from flask import Blueprint, render_template, request, make_response
from models.alert import Alert

alert_blueprint = Blueprint("alerts", __name__)


@alert_blueprint.route("/")
def index():
    alerts = Alert.find_all()
    return render_template("alerts/index.html", alerts=alerts)


@alert_blueprint.route("/new", methods=["GET", "POST"])
def new_alert():
    if request.method == "POST":
        item_id = request.form["item_id"]
        price_limit = request.form["price_limit"]

        Alert(item_id, price_limit).save_to_mongo()
        return make_response(index())

    return render_template("alerts/new_alert.html")
