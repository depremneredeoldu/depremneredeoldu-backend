from app.api.endpoints import earthquake
from app.core.security import check_api_key
from fastapi import APIRouter, Security

api_router = APIRouter(dependencies=[Security(check_api_key)])
api_router.include_router(earthquake.router, tags=["earthquake"])
