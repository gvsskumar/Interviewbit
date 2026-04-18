from fastapi import FastAPI, Request
from app.api.routes import router
from app.db.redis import redis_client
from app.middleware.rate_limiter import RateLimiter

app = FastAPI()

rate_limiter = RateLimiter(redis_client)

@app.middleware("http")
async def limit_requests(request: Request, call_next):
    await rate_limiter(request)
    response = await call_next(request)
    return response

app.include_router(router)