from flask import Flask, render_template
from flask_restful import Api
import requests

import os

# intern package
from db import db
from config import database_name, url_api_backend
from resources.earthquake import Earthquake, EarthquakesList


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", f"sqlite:///{database_name}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
api = Api(app)

api.add_resource(Earthquake, "/earthquake/<int:id_>")
api.add_resource(EarthquakesList, "/earthquakes")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
