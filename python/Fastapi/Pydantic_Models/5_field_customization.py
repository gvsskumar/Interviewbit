# Field Customization (Field)
    # username → min 3, max 10 chars
    # price → must be > 0
    # Add description
from pydantic import BaseModel, Field

class Product(BaseModel):
    username: str = Field(min_length=3, max_length=10, description="User name")
    price: float = Field(gt=0, description="Product price")