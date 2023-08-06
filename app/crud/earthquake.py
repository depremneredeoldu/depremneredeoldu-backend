from sqlalchemy.orm import Session

from app.models.earthquake import Earthquake
from app.schemas.earthquake import EarthquakeModel
from datetime import datetime
from fastapi.responses import JSONResponse
from typing import List, Dict


def get_earthquake(db: Session, earthquake_id: str) -> Dict[str, str]:
    return db.query(Earthquake).filter(Earthquake.earthquake_id == earthquake_id).first()


def get_earthquakes(db: Session, limit: int) -> List[Dict[str, str]]:
    if limit is None:
        return db.query(Earthquake).all()

    return db.query(Earthquake).limit(limit).all()


def create_earthquake(db: Session, earthquake: EarthquakeModel) -> None:
    earthquake_dict = earthquake.dict()
    # date formating
    earthquake_dict["date"] = datetime.strptime(earthquake_dict["date"], "%Y.%m.%d")

    earthquake_db_obj = Earthquake(**earthquake_dict)
    try:
        db.add(earthquake_db_obj)
        db.commit()
        db.refresh(earthquake_db_obj)
    except Exception as exc:  # noqa
        return JSONResponse({"message": "An error occurred while saving to the db."}, 500)
