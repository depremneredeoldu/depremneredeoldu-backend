from sqlalchemy.orm import load_only
from ma import ma
from models.earthquake import EarthquakeModel


class EarthquakeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EarthquakeModel
        load_only = ("id",)
        dump_only = ("id",)
        load_instance = True
