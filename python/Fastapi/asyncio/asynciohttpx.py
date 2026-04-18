import Fastapi.asyncio.asynciohttpx as asynciohttpx
import asyncio

async def fetch_data():
    async with asynciohttpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/users")
        return response.json()

result = asyncio.run(fetch_data())
print(result)