import sqlite3
from hashlib import sha256
import secrets
import json

def userExists(phone):
    try:
        connection = sqlite3.connect("WalkieTalkie.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE phone = ?", (phone,))
        result = cursor.fetchall()

        connection.close()

        return bool(len(result))
    except:
        return False


def addUser(phone, name, username, password):
    try:
        connection = sqlite3.connect("WalkieTalkie.db")
        cursor = connection.cursor()

        password = sha256(password.encode("UTF-8")).hexdigest()

        cursor.execute("INSERT INTO users (phone, name, username, password) VALUES (?, ?, ?, ?)", (phone, name, username, password,))
        connection.commit()

        connection.close()


        addDialogList(username)


        return "User registered!"
    except:
        return "Error: Can not register user!"


def checkPassword(phone, password):
    password = sha256(password.encode("UTF-8")).hexdigest()

    connection = sqlite3.connect("WalkieTalkie.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE phone = ?", (phone,))
    result = cursor.fetchall()

    Meta = []

    for x in result:
        Meta.append(x)

    dataPassword = Meta[0][4]

    connection.close()

    return secrets.compare_digest(password, dataPassword)


def setPassword(phone, newpassword):
    try:
        newPass = sha256(newpassword.encode("UTF-8")).hexdigest()

        connection = sqlite3.connect("WalkieTalkie.db")
        cursor = connection.cursor()

        cursor.execute("UPDATE users SET password = ? WHERE phone = ?", (newPass, phone,))

        connection.commit()

        connection.close()

        return True

    except:
        return False



def getLastID():
    cursor = sqlite3.connect("WalkieTalkie.db").cursor()
    result = cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='users'").fetchall()[0][0]

    print(result)


def addDialogList(username):

        connection = sqlite3.connect("WalkieTalkie.db")
        cursor = connection.cursor()

        cursor.execute(f"CREATE TABLE {username} (userchat TEXT)")

        connection.commit()
        connection.close()


def getDialogs(username):
    connection = sqlite3.connect("WalkieTalkie.db")
    cursor = connection.cursor()

    result = cursor.execute(f"SELECT userchat FROM {username}").fetchall()

    connection.commit()
    connection.close()

    response = []

    for user in result:
        response.append(user[0])

    return response



def getUsernameByPhone(phone):
    connection = sqlite3.connect("WalkieTalkie.db")
    cursor = connection.cursor()

    result = cursor.execute("SELECT username FROM users WHERE phone = ?", (phone,)).fetchall()[0][0]

    connection.commit()
    connection.close()

    return result

def getUsernameByPhone(phone):
    connection = sqlite3.connect("WalkieTalkie.db")
    cursor = connection.cursor()

    result = cursor.execute("SELECT username FROM users WHERE phone = ?", (phone,)).fetchall()[0][0]

    connection.commit()
    connection.close()

    return result


