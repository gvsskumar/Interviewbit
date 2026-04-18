from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    data = {
        "item_id": item_id,
        "name": "Laptop",
        "price": 50000
    }

    return {
        "status": "success",
        "data": data
    }