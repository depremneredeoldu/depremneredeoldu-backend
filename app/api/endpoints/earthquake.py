from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse
from google.cloud import firestore_v1

from app.core.database import get_firestore_db_object
from app.core.security import check_api_key_post_endpoints
from app.crud import earthquake as earthquake_crud
from app.schemas.earthquake import EarthquakeModel

router = APIRouter()


@router.get("/earthquakes")
async def get_earthquakes(
    db: firestore_v1.client.Client = Depends(get_firestore_db_object), limit: int = None
):
    all_earthquakes_obj = earthquake_crud.get_earthquakes(db=db, limit=limit)
    return {
        "earthquakes": [each_earthquake for each_earthquake in all_earthquakes_obj],
        "limit": limit,
    }


@router.post("/earthquake")
async def create_earthquake(
    earthquake: EarthquakeModel,
    db: firestore_v1.client.Client = Depends(get_firestore_db_object),
    api_key: str = Security(check_api_key_post_endpoints),
) -> JSONResponse:
    earthquake_obj = earthquake_crud.get_earthquake(
        db=db, earthquake_id=earthquake.earthquake_id
    )
    if earthquake_obj is not None:
        return JSONResponse({"message": "Earthquake already exists."}, 409)

    earthquake_crud.insert_earthquake(db=db, earthquake=earthquake)
    return JSONResponse({"message": "Earthquake added successfully."}, 201)
