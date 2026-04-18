# Create an API model to validate:
    # name → required string
    # age → integer (must be > 18)
    # email → valid email format

from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str
    age: int = Field(gt=18)
    email: EmailStr