from getpass import getuser
from conDB import MyDB as db


class Action:
    def getUser():
        data = db.userAll()
        return data

    def getUserbyID(userID):
        data = db.getUserByID(userID)
        return data

    def getUserbyID2(userID):
        data = db.getUserbyID2(userID)
        return data

    def getUserByUsername(username):
        data = db.getUserByUsername(username)
        return data

    def addUser(user):
        ID = db.addUser(user)
        data = db.getUserByID(ID)
        return data

    def login(user):

        getUser = db.login(user)
        # data = {
        #     "user":getUser,
        #     "error":False
        # }
        # return data
        return getUser

    def changPassById(ID, password):
        data = db.changPassById(ID, password)
        if data["error"] == False:
            getUser = db.getUserByID(ID)
            return getUser
        else:
            error = []
            error.append({"error": False})
            return error

    def dleteUser(user):
        data = db.dleteUser(user)
        return data

    def dleteUserbyUsername(user):
        data = db.dleteUserbyUsername(user)
        return data

    def changPassByUsername(username, password):
        data = db.changPassByUsername(username, password)
        if data["error"] == False:
            getUser = db.getUserByUsername(username)
            return getUser
        else:
            error = []
            error.append({"error": False})
            return error

    def getHW():
        data = db.getHW()
        return data
    
    def getHWByID(ID):
        data = db.getHWByID(ID)
        return data

    def getHWByName(name):
        data = db.getHWByName(name)
        return data

    def addHW(name, hw_name, status, value):
        ID = db.addHW(name, hw_name, status, value)
        data = db.getHWByID(ID)
        return data
    
    def updateStatusHW(name, status):
        error = db.updateStatusHW(name,status)
        data = db.getHWByName(name)
        return data
    
    def updateValueHW(name, value):
        error = db.addHW(name,value)
        data = db.updateValueHW(name)
        return data
