from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/data")
async def get_data():
    await asyncio.sleep(2)  # non-blocking
    return {"msg": "done"}