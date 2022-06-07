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


# ------------- routh ---------
# ----------------- users ------------------
@app.post("/api/login")
def login(user: User):
    data = ac.login(user)
    return data


@app.get("/")
async def api_con():
    con = {"Start": "Success"}
    error = []
    error.append(con)
    error.append({"error": False})
    return error


@app.get("/con")
async def api_con():
    con = {"Con": "Success"}
    error = []
    error.append(con)
    error.append({"error": False})
    return error


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
async def delete_user(user: User):
    data = ac.dleteUser(user)
    return data


@app.post("/api/delete_user_by_user_name")
async def delete_user_by_user_name(user: User):
    data = ac.dleteUserbyUsername(user)
    return data


# --------------- HW ------------------


@app.get("/hw")
async def hw():
    data = ac.getHW()
    return data


@app.get("/hw/get_by_id")
async def hw_get_by_id(ID):
    data = ac.getHWByID(ID)
    return data


@app.get("/hw/get_by_name")
async def hw_get_by_name(name):
    data = ac.getHWByName(name)
    return data


@app.get("/hw/get_by_name_and_hw_name")
async def hw_get_by_name(name, hw_name):
    data = ac.getHWByNameAndHWName(name, hw_name)
    return data


@app.get("/hw/add_hw")
async def add_hw(name, hw_name, status, value):
    data = ac.addHW(name, hw_name, status, value)
    return data


@app.get("/hw/update_status")
async def update_status(ID, status):
    data = ac.updateStatusHW(ID, status)
    return data


@app.get("/hw/update_value")
async def update_value(ID, value):
    data = ac.updateValueHW(ID, value)
    return data


@app.get("/hw/update_status_value")
async def update_status_value(ID, status, value):
    data = ac.updateStatusAndValueHW(ID, status, value)
    return data


@app.get("/hw/delete")
async def hw_delete(ID):
    data = ac.udeleteHW(ID)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
