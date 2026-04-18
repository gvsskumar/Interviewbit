from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -----------------------------
# Pydantic Model
# -----------------------------
class Address(BaseModel):
    city: str
    state: str
    pincode: str


class User(BaseModel):
    name: str
    phone: str
    age: int
    is_active: bool = True
    address: Address
    hobbies: List[str] = []


# -----------------------------
# Serialization Example
# -----------------------------
@app.get("/serialize")
def serialize_user():
    user = User(
        name="Satya",
        phone="1234567890",
        age=30,
        address=Address(
            city="Hyderabad",
            state="Telangana",
            pincode="500001"
        ),
        hobbies=["coding", "reading"]
    )

    return {
        "dict_output": user.model_dump(),      # Convert to Python dict
        "json_output": user.model_dump_json()       # Convert to JSON string
    }


# -----------------------------
# Deserialization Example
# -----------------------------
@app.post("/deserialize")
def deserialize_user(user: User):
    # FastAPI automatically converts JSON → Pydantic model

    return {
        "message": "User received successfully",
        "name": user.name,
        "phone": user.phone,
        "city": user.address.city,
        "hobbies": user.hobbies
    }