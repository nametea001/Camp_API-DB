from conDB import MyDB as db

class Action:
    def getUser():
        data = db.userAll()
        return data

    def getUserbyID(userID):
        data =  db.someUserByID(userID)
        return data

    def getUserByUsername(username):
        data =  db.getUserByID(username)
        return data
    
    def addUser(user):
        ID = db.addUser(user)
        return ID
    
    def login(user):
        
        getUser = db.login(user)
        # data = {
        #     "user":getUser,
        #     "error":False
        # }
        # return data
        return getUser
        
