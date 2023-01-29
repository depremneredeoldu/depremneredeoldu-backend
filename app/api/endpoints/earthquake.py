from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.schemas.earthquake import EarthquakeModel
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.database import Base, engine
from app.crud import earthquake as earthquake_crud

Base.metadata.create_all(bind=engine)
router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/earthquakes")
async def get_all_earthquakes(db: Session = Depends(get_db)):
    all_earthquakes_obj = earthquake_crud.get_all_earthquakes(db=db)
    return {"earthquakes": [each_earthquake for each_earthquake in all_earthquakes_obj]}


@router.post("/earthquake")
async def create_earthquake(
    earthquake: EarthquakeModel, db: Session = Depends(get_db)
) -> JSONResponse:
    earthquake_obj = earthquake_crud.get_earthquake(db=db, earthquake_id=earthquake.earthquake_id)
    if earthquake_obj:
        return JSONResponse({"message": "Earthquake already exists."}, 409)

    earthquake_crud.create_earthquake(db=db, earthquake=earthquake)
    return JSONResponse({"message": "Earthquake added successfully."}, 201)
