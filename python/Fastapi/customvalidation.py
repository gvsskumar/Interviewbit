from pydantic import field_validator,BaseModel

class Product(BaseModel):
    name: str
    price: float

    @field_validator("name")
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value