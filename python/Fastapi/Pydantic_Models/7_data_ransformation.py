from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str

    @field_validator('name')
    def uppercase_name(cls, v):
        return v.upper()