from flask import Flask
from flask_restful import Api
from ma import ma
import os

# intern package
from db import db
from config import database_name
from resources.earthquake import Earthquake, EarthquakesList


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", f"sqlite:///{database_name}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
api = Api(app)

api.add_resource(Earthquake, "/earthquake/<int:id_>", endpoint="earthquake")
api.add_resource(Earthquake, "/earthquake", endpoint="earthquake_post")
api.add_resource(EarthquakesList, "/earthquakes", endpoint="earthquakes")


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
