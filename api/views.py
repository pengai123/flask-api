from flask import Blueprint, jsonify, request
from . import mongo
import json
from bson import json_util

main = Blueprint("main", __name__)
users = mongo.db.users


@main.route("/")
def homepage():
    return "welcome to homepage"


@main.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    print("db users", users)
    user = users.insert_one(new_user)
    print("user", json.dumps(user, default=json_util.default))
    return jsonify("qweasd")


@main.route("/users")
def all_users():
    return jsonify("qwe")
