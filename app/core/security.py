from fastapi import Header, HTTPException

from app.core.config import settings


async def verify_internal_api_key(
    x_internal_api_key: str = Header(...)
):

    if x_internal_api_key != settings.INTERNAL_API_KEY:

        raise HTTPException(
            status_code=401,
            detail="Invalid internal API key"
        )