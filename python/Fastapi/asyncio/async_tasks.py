import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 Done")

async def task2():
    await asyncio.sleep(1)    
    print("Task async tasks")

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())