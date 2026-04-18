import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # simulate API call
    print("Data fetched")
    return "DATA"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())