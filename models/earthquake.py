from db import db


class EarthquakeModel(db.Model):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80))
    time = db.Column(db.String(80))
    latitude = db.Column(db.String(80))
    longitude = db.Column(db.String(80))
    depth = db.Column(db.String(80))
    magnitude = db.Column(db.String(80))
    location = db.Column(db.String(150))

    def __init__(
            self,
            date,
            time,
            latitude,
            longitude,
            depth,
            magnitude,
            location
    ):
        self.date = date
        self.time = time
        self.latitude = latitude
        self.longitude = longitude
        self.depth = depth
        self.magnitude = magnitude
        self.location = location

    def json(self):
        return {
            "date": self.date,
            "time": self.time,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "depth": self.depth,
            "magnitude": self.magnitude,
            "location": self.location
        }

    @classmethod
    def find_by_id(cls, id_):
        return cls.query.filter_by(id=id_).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


