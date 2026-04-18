from fastapi import BackgroundTasks,FastAPI
app = FastAPI()

def send_email():
    print("Email sent")

@app.post("/order")
#=============================#
async def create_order(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email)
    return {"message": "Order placed"}

from fastapi import BackgroundTasks

def send_email():
    print("Email sent")

@app.post("/order")
async def create_order(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email)
    return {"message": "Order placed"}