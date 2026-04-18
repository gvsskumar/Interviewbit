from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

# 🔍 Advanced Example (Real Interview Level)
# http://127.0.0.1:8000/search?keyword=phone&min_price=10000&max_price=50000&in_stock=true
@app.get("/search")
def search_items(
    keyword: str,
    min_price: int = 0,
    max_price: int = 100000,
    in_stock: bool = True
):
    return {
        "keyword": keyword,
        "price_range": [min_price, max_price],
        "available": in_stock
    }

# http://127.0.0.1:8000/products?category=mobile&price=20000
@app.get("/products")
def get_products(category: str, price: int):
    return {
        "category": category,
        "price": price
    }

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/sync")
def sync_api():
    return {"msg": "sync"}

@app.get("/async")
async def async_api():
    return {"msg": "async"}

@app.post("/user")
def create_user(name: str):
    return {"user": name}

@app.get("/user/{id}")
def get_user(id: int):
    return {"id": id}

@app.get("/slow")
async def slow_api():
    await asyncio.sleep(3)
    return {"message":"completed"}

@app.get("/fast")
async def fast_api():
    return {"message": "Quick response"}

class User(BaseModel):
    name:str
    age:int

@app.get('/post')
def post_user(user:User):
    return {"message":user}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}