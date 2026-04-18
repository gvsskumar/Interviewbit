# Validate password:
    # Min length 8
    # Must contain at least 1 number
from pydantic import BaseModel, field_validator

class User(BaseModel):
    password: str

    @field_validator('password')
    def strong_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password too short")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain a number")
        return value