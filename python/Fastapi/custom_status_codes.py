from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "TV"}
]

# ✅ CREATE → 201
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    items.append(item)
    return {
        "status": "success",
        "data": item
    }

# ✅ DELETE → 204
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(index)
            return  # ❗ No response body for 204

    raise HTTPException(status_code=404, detail="Item not found")