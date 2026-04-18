# Create reusable pagination:
    # page
    # limit

from fastapi import Depends,FastAPI
app = FastAPI()

def pagination(page: int = 1, limit: int = 10):
    return {"page": page, "limit": limit}

@app.get("/items")
def get_items(paging=Depends(pagination)):
    return paging