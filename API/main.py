from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

# class User(BaseModel):
#     username: Optional[str]
#     password: Optional[str]

# # ------------- routh ---------
# @app.post("/api/login")
# def api_login(user: User):
#     return True

@app.get("/con")
async def api_con():
    con = {"Con":"Success"}
    return con

@app.get("/api/get")
async def api_test_get(massage):
    test = massage
    return test

@app.post("/api/post")
async def api_test_post(massage):
    test = massage
    return test

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)