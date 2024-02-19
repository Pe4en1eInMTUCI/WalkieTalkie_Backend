
import sqlite3
from hashlib import sha256
import secrets


def userExists(username):
    try:
        connection = sqlite3.connect("WalkieTalkie.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
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


