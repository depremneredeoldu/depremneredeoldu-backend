from app.api.endpoints import earthquake

from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(earthquake.router, tags=["earthquake"])
