# ✅ Challenge 1: Build a CRUD API (Most Common)
from fastapi import FastAPI,HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
class Product(BaseModel):
    id: int
    name: str
    price: int
    qty: int

products = [{"id":1,"name":'Laptop',"price":50000,"qty":2},
            {"id":2,"name":'TV',"price":20000,"qty":5}]

#Products
@app.post('/create',status_code=201)
def create_product_Modal(product:Product):
     # Duplicate check
    for p in products:
        if p["id"] == product.id:
            raise HTTPException(status_code=400, detail="Product ID already exists")

    # Convert to dict
    products.append(product.model_dump())

    return {
        "message": "Successfully Inserted",
        "product": product
    }

@app.get('/products')
def get_product_modal(
    id:Optional[int]=None,
    name:Optional[str]=None,
    price:Optional[int]=None,
    qty:Optional[int]=None
    ):
    result = products
    if id is not None:
        result = [p for p in result if p['id']==id]
    if name is not None:
        result = [p for p in result if p['name'].lower()==name.lower() ]
    if price is not None:
        result = [p for p in result if p['price']==price]  
    if qty is not None:
        result = [p for p in result if p['qty']==qty]        
    if not result:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return result

@app.put('/update/{id}')
def update_product_modal(id: int, updated_product: Product):

    # Find product
    for index, p in enumerate(products):
        if p["id"] == id:

            # Optional: prevent ID mismatch
            if updated_product.id != id:
                raise HTTPException(status_code=400, detail="ID mismatch")

            # Update product
            products[index] = updated_product.model_dump()

            return {
                "message": "Successfully Updated",
                "product": products[index]
            }
    raise HTTPException(status_code=404, detail="Product Not Found")    

@app.delete('/products/{id}')
def delete_product_modal(id: int):

    for index, p in enumerate(products):
        if p["id"] == id:
            deleted_product = products.pop(index)

            return {
                "message": "Successfully Deleted",
                "product": deleted_product
            }

    # If not found
    raise HTTPException(status_code=404, detail="Product Not Found")