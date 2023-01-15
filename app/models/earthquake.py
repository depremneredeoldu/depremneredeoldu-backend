from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from app.core.database import Base


class EarthquakeModel(Base):
    __tablename__ = "earthquakes"

    id = Column(Integer, primary_key=True)
    earthquake_id = Column(String(80), nullable=False, unique=True)
    date = Column(Date, nullable=False)
    time = Column(String(80), nullable=False)
    latitude = Column(String(80), nullable=False)
    longitude = Column(String(80), nullable=False)
    depth = Column(String(80), nullable=False)
    magnitude = Column(String(80), nullable=False)
    location = Column(String(150), nullable=False)
