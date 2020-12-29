from flask_restful import Resource, reqparse

# intern package
from models.earthquake import EarthquakeModel


class Earthquake(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("date", required=True, help="This field cannot be left blank!")
    parser.add_argument("time", required=True, help="This field cannot be left blank!")
    parser.add_argument("latitude", required=True, help="This field cannot be left blank!")
    parser.add_argument("longitude", required=True, help="This field cannot be left blank!")
    parser.add_argument("depth", required=True, help="This field cannot be left blank!")
    parser.add_argument("magnitude", required=True, help="This field cannot be left blank!")
    parser.add_argument("location", required=True, help="This field cannot be left blank!")

    def get(self, id_):
        earthquake = EarthquakeModel.find_by_id(id_)
        if earthquake:
            return earthquake.json()
        return {"message": "Item not found."}, 404

    def post(self, id_):
        data = Earthquake.parser.parse_args()
        if EarthquakeModel.find_by_id(id_):
            return {"message": "Item already exists."}, 400

        earthquake = EarthquakeModel(**data)

        try:
            earthquake.save_to_db()
        except:
            return {"message": "An error occurred while saving to the db."}, 500

        return earthquake.json(), 201


class EarthquakesList(Resource):
    def get(self):
        return {"earthquakes": [earthquake.json() for earthquake in EarthquakeModel.query.all()]}


