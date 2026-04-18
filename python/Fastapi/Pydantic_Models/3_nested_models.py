# User with Address:
    # User → name, email
    # Address → city, pincode

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pincode: str

class User(BaseModel):
    name: str
    email: str
    address: Address