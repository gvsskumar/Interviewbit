from fastapi import FastAPI,HTTPException
import json
import os
from typing import Optional

app = FastAPI()

# Set BASE DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join('./mock/user.json')

# Load the JSON file
with open(file_path,'r',encoding='utf-8') as file:
    USERS = json.load(file)

# Set Dectonary
USER_ID = {user['id']:user for user in USERS}
# Write a API
@app.get('/users')
def get_user_modal(
    id:Optional[int]=None,
    role:Optional[str]=None,
    company:Optional[str] =None,
    city:Optional[str]=None
    ):
    result = USERS
    if id is not None:
        result = [u for u in result 
                  if u.get('id')==id]

    if role is not None:
        result = [ u for u in result
                   if u.get('role','').lower()==role.lower()] 
        
    if company is not None:
        result = [ u for u in result
                   if u.get('company',{}).get('name','').lower()==company.lower()]     
    if city is not None:
        result = [ u for u in result
                   if u.get('address',{}).get('city','').lower()==city.lower()]         
    
    if not result:
        raise HTTPException(status_code=404,detail="User Not Found")
    return result
           