from flask import Blueprint, jsonify, request
from . import mongo

main = Blueprint("main", __name__)
users = mongo.db.users

@main.route("/")
def homepage():
	return "welcome to homepage"

@main.route("/add_user", methods=["POST"])
def add_user():
	new_user = request.get_json()
	print("db users", users)
	# user= users.insert_one(new_user)
	return jsonify(new_user)

@main.route("/users")
def users():
	return jsonify("qwe")