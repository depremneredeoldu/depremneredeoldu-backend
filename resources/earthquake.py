from flask_restful import Resource
from flask import request
from flask_cors import cross_origin
from marshmallow import ValidationError

# intern package
from models.earthquake import EarthquakeModel
from schemas.earthquake import EarthquakeSchema

earthquake_schema = EarthquakeSchema()


class Earthquake(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def get(self, id_):
        earthquake = EarthquakeModel.find_by_id(id_)
        if earthquake:
            return earthquake_schema.dump(earthquake)
        return {"message": "Item not found."}, 404

    def post(self):
        try:
            earthquake = earthquake_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if EarthquakeModel.find_by_id(earthquake.earthquake_id):
            return {"message": "Item already exists."}, 400

        try:
            earthquake.save_to_db()
        except:
            return {"message": "An error occurred while saving to the db."}, 500

        return earthquake_schema.dump(earthquake), 201


class EarthquakesList(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def get(self):
        return {"earthquakes": [earthquake_schema.dump(earthquake) for earthquake in EarthquakeModel.query.all()]}
