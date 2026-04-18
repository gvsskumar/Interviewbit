from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    name: str

class Users(BaseModel):
    users: List[User]