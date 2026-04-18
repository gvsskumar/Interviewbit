from fastapi import Request
from fastapi.responses import JSONResponse

class RateLimiter:

    def __init__(self, redis, limit=5, window=60):
        self.redis = redis
        self.limit = limit
        self.window = window

    async def __call__(self, request: Request):
        ip = request.client.host
        key = f"rate:{ip}"

        count = await self.redis.incr(key)

        if count == 1:
            await self.redis.expire(key, self.window)

        if count > self.limit:
            return JSONResponse(
    status_code=429,
    content={"detail": "Too many requests"}
)