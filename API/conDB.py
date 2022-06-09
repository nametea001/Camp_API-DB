import mysql.connector
import datetime


def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="api",
        password="api",
        database="api",
    )
    return mydb


class MyDB:
    def userAll():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getUserByID(userID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE id = {}".format(userID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getUserbyID2(userID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT id, username FROM users WHERE id = {}".format(userID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getUserByUsername(username):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE username = '{}'".format(username)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def addUser(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO users (id, username, password, name, last_name, address, user_role_id) VALUES ({}, '{}', '{}', '{}', '{}', '{}', 2)".format(
            user.ID,
            user.username,
            user.password,
            user.name,
            user.last_name,
            user.address,
        )
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def addUser2(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO users (username, password, name, last_name, address, user_role_id) VALUES ('{}', '{}', '{}', '{}', '{}', 2)".format(
            user.username,
            user.password,
            user.name,
            user.last_name,
            user.address,
        )
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def login(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT id, username, user_role_id FROM users WHERE username = '{}' AND password = '{}'".format(
            user.username, user.password
        )
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def changPassById(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET password = '{}' WHERE id = {}".format(
            user.password, user.ID
        )
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error

    def changHistory(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET name = '{}', last_name = '{}', address = '{}', WHERE id = {}".format(
            user.name, user.last_name, user.address, user.ID
        )
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error

    def changPassByUsername(username, password):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET password = '{}' WHERE username = '{}'".format(
            password, username
        )
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error

    def dleteUser(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM users WHERE id = {}".format(user.ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        # print(mycursor.rowcount, "record(s) deleted")
        error = []
        error.append({"error": False})
        return error

    def dleteUserbyUsername(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM users WHERE username = '{}'".format(user.username)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        # print(mycursor.rowcount, "record(s) deleted")
        error = []
        error.append({"error": False})
        return error

    # ------------------ hW --------------
    def getHW():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hw "
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getHWByID(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hw WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getHWByName(name):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hw WHERE name = '{}'".format(name)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getHWByNameAndHWName(name, hw_name):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hw WHERE name = '{}' AND hw_name = '{}' ".format(
            name, hw_name
        )
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def addHW(name, hw_name):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hw (name, hw_name, status, value) VALUES ('{}', '{}', 'OFF', '0')".format(
            name, hw_name
        )
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def updateStatusHW(ID, status):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hw SET status = '{}' WHERE id = {}".format(status, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error

    def updateValueHW(ID, value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hw SET value = '{}' WHERE id = {}".format(value, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error

    def updateStatusAndValueHW(ID, status, value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hw SET status = '{}', value = '{}' WHERE id = {}".format(
            status, value, ID
        )
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error

    def deleteHW(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hw WHERE id = {}".format(ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error
