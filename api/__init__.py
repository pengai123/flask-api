from flask import Flask
from flask_pymongo import PyMongo


mongo = PyMongo()

def create_app():
	app = Flask(__name__)
	
	app.config["MONGO_URI"] = "mongodb+srv://mongodb:mongodb@cluster0.mhwte.mongodb.net/flask-api?retryWrites=true&w=majority"
	
	mongo.init_app(app)

	from .views import main
	app.register_blueprint(main)

	return app