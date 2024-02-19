
import sqlite3
from hashlib import sha256
import secrets


def userExists(username):
    try:
        connection = sqlite3.connect("./WalkieTalkie.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = cursor.fetchall()

        connection.close()

        return bool(len(result))
    except:
        return False


def addUser(phone, username, password):
    try:
        connection = sqlite3.connect("./WalkieTalkie.db")
        cursor = connection.cursor()

        password = sha256(password.encode("UTF-8".hexdigest)).hexdigest()

        cursor.execute("INSERT INTO users VALUES phone, username, password (?, ?, ?)", (phone, username, password,))

        connection.close()
        return "User added!"
    except:
        return "Error!"



addUser("79778614427", "pe4en1e", "somepassword")