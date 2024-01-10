from fastapi import APIRouter, Security
from fastapi.responses import JSONResponse

from app.core.security import check_api_key_post_endpoints
from app.crud import earthquake as earthquake_crud
from app.schemas.earthquake import EarthquakeModel

router = APIRouter()


@router.get("/earthquake/{earthquake_id}")
async def get_earthquake(earthquake_id: int):
    """Extract earthquake information by earthquake id"""
    results = earthquake_crud.get_earthquake(earthquake_id=int(earthquake_id))
    if results.total_rows == 0:
        return JSONResponse({"message": "Earthquake not found."}, 404)

    return {"earthquake": [each_earthquake for each_earthquake in results]}


@router.get("/earthquakes")
async def get_earthquakes(limit: int = None):
    """Extract all earthquakes for a given limit"""
    all_earthquakes_obj = earthquake_crud.get_earthquakes(limit=limit)
    return {
        "earthquakes": [each_earthquake for each_earthquake in all_earthquakes_obj],
        "limit": limit,
    }


@router.post("/earthquake")
async def create_earthquake(
    earthquake: EarthquakeModel,
    api_key: str = Security(check_api_key_post_endpoints),  # noqa,
) -> JSONResponse:
    """Add new earthquake"""
    results = earthquake_crud.get_earthquake(earthquake_id=earthquake.earthquake_id)
    if results.total_rows > 0:
        return JSONResponse({"message": "Earthquake already exists."}, 409)

    earthquake_crud.create_earthquake(earthquake=earthquake)
    return JSONResponse({"message": "Earthquake added successfully."}, 201)
