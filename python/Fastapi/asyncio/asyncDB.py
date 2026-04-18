from fastapi import FastAPI,Depends

app = FastAPI()

def get_db():
    return {"msg":"DB connected"}

@app.get("/users")
async def get_users(db=Depends(get_db)):
    result = await db.fetch("SELECT * FROM users")
    return result