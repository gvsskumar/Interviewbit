from fastapi import FastAPI

app = FastAPI()

# ✅ Static route FIRST
@app.get("/users/me")
def get_current_user():
    return {"user": "current user"}

# ✅ Dynamic route AFTER
@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id}