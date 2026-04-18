from fastapi import Query,HTTPException,FastAPI

app = FastAPI()
items = []
@app.get("/items/{item_id}")
def get_item(
    item_id: int,
    discount: int = Query(0, ge=0, description="Discount must be >= 0")
):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    item = items[item_id]
    final_price = item["price"] - discount

    return {
        "item_id": item_id,
        "final_price": final_price
    }