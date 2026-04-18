from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {
    1: {"name": "Laptop", "price": 50000}
}

@app.get("/items/{item_id}")
def get_item(item_id: int):

    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return {
        "status": "success",
        "data": items[item_id]
    }