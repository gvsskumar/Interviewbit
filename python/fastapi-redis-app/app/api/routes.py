from fastapi import APIRouter, Depends
from app.dependencies import get_redis_dep
from app.services.cache_service import CacheService

router = APIRouter()

@router.get("/data")
async def get_data(redis=Depends(get_redis_dep)):
    cache = CacheService(redis)

    cached = await cache.get("data")
    if cached:
        return {"source": "cache", "data": cached}

    # Simulate DB call
    data = {"message": "Hello from DB"}

    await cache.set("data", data, ttl=30)
    return {"source": "db", "data": data}