from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    # Before request
    print(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    # After response
    process_time = time.time() - start_time
    print(f"Response time: {process_time:.4f}s")

    return response