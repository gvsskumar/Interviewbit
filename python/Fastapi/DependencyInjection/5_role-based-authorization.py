from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional

app = FastAPI()

# -----------------------------------
# Mock Token Verification Dependency
# -----------------------------------
def verify_token(token: Optional[str] = None):
    """
    Simulates token verification.
    In real-world, this will decode JWT token.
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing"
        )

    # Mock logic
    if token == "admin-token":
        return {"username": "satya", "role": "admin"}
    elif token == "user-token":
        return {"username": "john", "role": "user"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


# -----------------------------------
# Get Current User
# -----------------------------------
def get_current_user(user_data=Depends(verify_token)):
    """
    Extract user from token
    """
    return user_data


# -----------------------------------
# Admin Only Dependency
# -----------------------------------
def admin_only(user=Depends(get_current_user)):
    """
    Allow only admin users
    """
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Admin access required"
        )
    return user


# -----------------------------------
# Public Endpoint
# -----------------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to API"}


# -----------------------------------
# User Endpoint
# -----------------------------------
@app.get("/user")
def user_dashboard(user=Depends(get_current_user)):
    return {
        "message": "Welcome User",
        "user": user
    }


# -----------------------------------
# Admin Endpoint (Protected)
# -----------------------------------
@app.get("/admin")
def admin_dashboard(user=Depends(admin_only)):
    return {
        "message": "Welcome Admin",
        "user": user
    }