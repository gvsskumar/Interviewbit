from fastapi import FastAPI,Depends

app = FastAPI()
# def pagination(page: int = 1, limit: int = 10):
#     return {"page": page, "limit": limit}

# @app.get("/items")
# def get_items(paging=Depends(pagination)):
#     return paging
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
        

@app.get('/user')
def get_user(db=Depends(get_db)):
    return {"db":db}