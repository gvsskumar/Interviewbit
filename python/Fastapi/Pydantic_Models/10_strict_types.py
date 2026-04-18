from pydantic import BaseModel, StrictInt

class User(BaseModel):
    age: StrictInt