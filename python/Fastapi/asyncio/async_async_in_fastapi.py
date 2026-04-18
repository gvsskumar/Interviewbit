from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/data")
async def get_data():
    await asyncio.sleep(2)
    return {"message": "Data fetched"}