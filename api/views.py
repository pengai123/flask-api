from flask import Blueprint, jsonify, request

main = Blueprint("main", __name__)
movie_list = []

@main.route("/")
def homepage():
	return "welcome to homepage"

@main.route("/add_movie", methods=["POST"])
def add_movie():
	new_movie = request.get_json()
	movie_list.append(new_movie)
	print("movie list", movie_list)
	return jsonify(movie_list)

@main.route("/movies")
def movies():
	return jsonify(movie_list)