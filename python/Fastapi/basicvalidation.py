from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request Body Model
class Product(BaseModel):
    name: str
    price: float

@app.post("/products")
def create_product(product: Product):
    return product