from pydantic import BaseModel


class EarthquakeModel(BaseModel):
    earthquake_id: str
    date: str
    time: str
    latitude: str
    longitude: str
    depth: str
    magnitude: str
    location: str
