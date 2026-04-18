# Authentication Dependency
# Validate token from header

from fastapi import Header, HTTPException, Depends,FastAPI

app = FastAPI()

def verify_token(token: str = Header(...)):
    if token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/secure")
def secure_api(token=Depends(verify_token)):
    return {"msg": "Authorized"}