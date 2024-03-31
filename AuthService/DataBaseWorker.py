import sqlite3
from hashlib import sha256
import secrets


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


def addUser(phone, username, password):
    try:
        connection = sqlite3.connect("WalkieTalkie.db")
        cursor = connection.cursor()

        password = sha256(password.encode("UTF-8")).hexdigest()

        cursor.execute("INSERT INTO users (phone, username, password) VALUES (?, ?, ?)", (phone, username, password,))
        connection.commit()

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

    dataPassword = Meta[0][3]

    connection.close()

    return secrets.compare_digest(password, dataPassword)
