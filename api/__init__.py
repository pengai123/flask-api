from flask import Flask
from flask_pymongo import PyMongo
import os

mongo = PyMongo()


def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.environ["MONGO_URI"]

    mongo.init_app(app)

    from .views import main

    app.register_blueprint(main)

    return app
