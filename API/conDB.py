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

    def changPassById(ID, password):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET password = '{}' WHERE id = {}".format(password, ID)
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
        sql = "SELECT * FROM hw WHERE name = '{}' OR hw_name = '{}' ".format(name, name)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def addHW(name, hw_name, status, value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hw (name, hw_name, status, value) VALUES ('{}', '{}', '{}', '{}')".format(
            name, hw_name, status, value
        )
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def updateStatusHW(name, status):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hw SET status = '{}' WHERE name = '{}'".format(status, name)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error
    
    def updateValueHW(name, value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hw SET value = '{}' WHERE name = '{}'".format(value, name)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        error = []
        error.append({"error": False})
        return error
