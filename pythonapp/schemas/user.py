# schemas/user.py
from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode = True