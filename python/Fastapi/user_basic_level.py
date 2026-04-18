from fastapi import FastAPI,HTTPException
import json
app = FastAPI()
# Initial Excuted Root Level '/'
@app.get('/')
def read_root():
    return {'message':'This is USer API response'}

# Display all user endpoint
@app.get('/user')
def get_user_modal():
    with open('./mock/user.json','r') as file:
        user = json.load(file)
    return user

# Display single user by id endpoint
@app.get('/user/{id}')
def get_userid_modal(id: int):
    with open('./mock/user.json','r',encoding='utf-8') as file:
        users = json.load(file)

        for user in users:
            if user['id'] == id:
                return user
        raise HTTPException(status_code=404,detail="User Not Found")    

# Display matched users by role property endpoint
@app.get('/users/{role}')
def get_userbyrole_modal(role:str):
    with open('./mock/user.json','r') as file:
        users = json.load(file)
    filtered_users = [user for user in users if user['role']==role]
    if not filtered_users:
        raise HTTPException(status_code=404,detail="User not found") 
    return filtered_users    

#Display users based on the nested-level property user["company"]["name"]
@app.get('/users')
def get_users_companyname_modal(company:str):
    with open('./mock/user.json','r') as file:
        users = json.load(file)

        result = [
          user for user in users
          if user["company"]["name"].lower() == company.lower()
        ]
    if not result:
        raise HTTPException(status_code=404,detail="User Not Found")
    return result    