# Create a reusable dependency that returns a common message.

from fastapi import FastAPI, Depends

app = FastAPI()

def common_params():
    return {"msg": "Hello from dependency"}

@app.get("/")
def read_root(data=Depends(common_params)):
    return data