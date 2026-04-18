# services/auth_service.py
from datetime import timedelta
from app.core.security import verify_password, create_token
from app.core.config import settings

def authenticate_user(db, username, password):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def generate_tokens(user):
    access_token = create_token(
        {"sub": user.username, "role": user.role},
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    refresh_token = create_token(
        {"sub": user.username},
        timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
    )

    return access_token, refresh_token