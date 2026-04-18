#Challenge 4: Optional Fields & Defaults
    # phone → optional
    # is_active → default True

from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: Optional[str] = None
    is_active: bool = True
