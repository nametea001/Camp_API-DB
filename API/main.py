from re import X
from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel
from typing import Optional

from action import Action as ac

app = FastAPI()


class User(BaseModel):
    ID: Optional[int]
    username: Optional[str]
    password: Optional[str]
    name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]


class User2(BaseModel):
    username: Optional[str]
    password: Optional[str]


# ------------- routh ---------
@app.post("/api/login")
def login(user: User2):
    data = ac.login(user)
    return data


@app.get("/")
async def api_con():
    con = {"Start": "Success"}
    return con

@app.get("/con")
async def api_con():
    con = {"Con": "Success"}
    return con


@app.get("/api/user_all")
async def user_all():
    data = ac.getUser()
    return data



@app.get("/api/user_by_id")
async def get_user_id(userID):
    data = ac.getUserbyID(userID)
    return data

@app.get("/api/user_by_id_2")
async def get_user_id_2(userID):
    data = ac.getUserbyID2(userID)
    return data


@app.get("/api/user_by_username")
async def get_user_username(username):
    data = ac.getUserByUsername(username)
    return data


@app.post("/api/add_user")
async def add_user(user: User):
    data = ac.addUser(user)
    return data


@app.post("/api/chang_password_by_id")
async def chang_password_by_id(ID, password):
    data = ac.changPassById(ID, password)
    return data

@app.post("/api/chang_password_by_username")
async def chang_password_by_username(username, password):
    data = ac.changPassByUsername(username, password)
    return data

@app.post("/api/delete_user")
async def delete_user(UserID):
    data = ac.DleteUser(UserID)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
