from fastapi import HTTPException,FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0, description="Price must be greater than 0")

@app.post("/products", status_code=201)
def create_product(product: Product):
    return {
        "message": "Product Created",
        "product": product
    }