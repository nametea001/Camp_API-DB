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
        if(data['error'] == False ):
            getUser = db.getUserByID(ID)
            return getUser
        else:
            return {"error": True}
    
    def changPassByUsername(username, password):
        data = db.changPassByUsername(username, password)
        if(data['error'] == False ):
            getUser = db.getUserByUsername(username)
            return getUser
        else:
            return {"error": True}


