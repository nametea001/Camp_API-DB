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

    def getHWByNameAndHWName(name, hw_name):
        data = db.getHWByNameAndHWName(name, hw_name)
        return data

    def addHW(name, hw_name, status, value):
        ID = db.addHW(name, hw_name, status, value)
        data = db.getHWByID(ID)
        return data

    def updateStatusHW(ID, status):
        error = db.updateStatusHW(ID, status)
        data = db.getHWByID(ID)
        return data

    def updateValueHW(ID, value):
        error = db.updateValueHW(ID, value)
        data = db.getHWByID(ID)
        return data

    def updateStatusAndValueHW(ID, status, value):
        error = db.updateStatusAndValueHW(ID, status, value)
        data = db.getHWByName(ID)
        return data

    def udeleteHW(ID):
        data = db.deleteHW(ID)
        return data