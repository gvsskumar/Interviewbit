from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Product API",
    description="API for managing products",
    version="1.0.0"
)

# Request Model with examples
class Product(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        description="Name of the product",
        example="Laptop"
    )
    price: float = Field(
        ...,
        gt=0,
        description="Price must be greater than 0",
        example=50000
    )

# API with documentation enhancements
@app.post(
    "/items",
    tags=["Items"],
    summary="Create a new product",
    description="This API creates a product with name and price",
    response_description="Created product details"
)
def create_item(product: Product):
    return {
        "status": "success",
        "data": product
    }