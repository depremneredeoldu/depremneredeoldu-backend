from db import db


class EarthquakeModel(db.Model):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    earthquake_id = db.Column(db.Integer, nullable=False, unique=True)
    date = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    latitude = db.Column(db.String(80), nullable=False)
    longitude = db.Column(db.String(80), nullable=False)
    depth = db.Column(db.String(80), nullable=False)
    magnitude = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(150), nullable=False)

    @classmethod
    def find_by_id(cls, id_):
        return cls.query.filter_by(earthquake_id=id_).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
