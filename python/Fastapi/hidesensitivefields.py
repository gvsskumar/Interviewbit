from fastapi import FastAPI
from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

app = FastAPI()

@app.post("/user", response_model=UserOut)
def create_user(user: UserIn):
    return user