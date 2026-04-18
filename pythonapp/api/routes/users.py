# api/routes/users.py
from fastapi import APIRouter, Depends
from app.api.deps import get_current_user, require_role

router = APIRouter(prefix="/users")

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return user

@router.get("/admin")
def admin_only(user=Depends(require_role("admin"))):
    return {"message": "Welcome Admin"}