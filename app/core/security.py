from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from app.core.config import settings

from .exceptions import APIKeyNotFound

api_key_header = APIKeyHeader(name=settings.API_KEY_HEADER_NAME, auto_error=False)

API_KEY_NOT_FOUND_ERR_MSG = "Are you sure to put API_KEY in your env file ?"


async def check_api_key_get_endpoints(
    api_key_header: str = Security(api_key_header),
) -> APIKeyHeader:
    if settings.API_KEY_GET is None:
        raise APIKeyNotFound(API_KEY_NOT_FOUND_ERR_MSG)

    if api_key_header == settings.API_KEY_GET:
        return api_key_header

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )


async def check_api_key_post_endpoints(
    api_key_header: str = Security(api_key_header),
) -> APIKeyHeader:
    if settings.API_KEY_POST is None:
        raise APIKeyNotFound(API_KEY_NOT_FOUND_ERR_MSG)

    if api_key_header == settings.API_KEY_POST:
        return api_key_header

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )
