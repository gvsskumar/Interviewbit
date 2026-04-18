from app.db.redis import get_redis

async def get_redis_dep():
    return await get_redis()