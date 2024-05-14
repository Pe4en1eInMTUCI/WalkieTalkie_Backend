import mysql.connector
import hashlib
import secrets

def phoneExists(phone):
    try:

        DataBase = mysql.connector.connect(
            host="147.45.138.238",
            port="3306",
            user="gen_user",
            password="Ib&c5<ysBY}l71",
            database="default_db"
        )

        cursor = DataBase.cursor()
        cursor.execute("SELECT * FROM users WHERE phone = %s", (phone,))
        result = cursor.fetchall()

        DataBase.close()

        return bool(len(result))
    except Exception as e:
        return f"Exception!\n\n{e}"


def usernameExists(username):
    try:
        DataBase = mysql.connector.connect(
            host="147.45.138.238",
            port="3306",
            user="gen_user",
            password="Ib&c5<ysBY}l71",
            database="default_db"
        )

        cursor = DataBase.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchall()

        DataBase.close()

        return bool(len(result))
    except Exception as e:
        return f"Exception!\n\n{e}"


def addUser(phone, username, password):
    try:
        DataBase = mysql.connector.connect(
            host="147.45.138.238",
            port="3306",
            user="gen_user",
            password="Ib&c5<ysBY}l71",
            database="default_db"
        )

        password = hashlib.sha256(password.encode('UTF-8')).hexdigest()

        cursor = DataBase.cursor()

        avatarLink = f"https://api.dicebear.com/8.x/initials/svg?seed={username}"

        cursor.execute("INSERT INTO users (phone, username, password, isOnline, avatar) VALUES (?, ?, ?, 1, ?)", (phone, username, password, avatarLink))

        DataBase.commit()
        DataBase.close()

        return True

    except Exception as e:
        return f"Exception!\n\n{e}"


def checkPassword(phone, password):
    try:
        DataBase = mysql.connector.connect(
            host="147.45.138.238",
            port="3306",
            user="gen_user",
            password="Ib&c5<ysBY}l71",
            database="default_db"
        )

        password = hashlib.sha256(password.encode('UTF-8')).hexdigest()

        cursor = DataBase.cursor()
        cursor.execute("SELECT * FROM users WHERE phone = ?", (phone,))
        result = cursor.fetchall()

        Meta = []

        for x in result:
            Meta.append(x)

        dataPassword = Meta[0][3]

        DataBase.close()

        return secrets.compare_digest(password, dataPassword)

    except Exception as e:
        return f"Exception!\n\n{e}"



def addDialogList(username):
    try:
        DataBase = mysql.connector.connect(
            host="147.45.138.238",
            port="3306",
            user="gen_user",
            password="Ib&c5<ysBY}l71",
            database="default_db"
        )

        cursor = DataBase.cursor()
        cursor.execute("CREATE TABLE ? (chatID INT AUTO_INCREMENT PRIMARY KEY, userID VARCHAR(255))", (username,))
        DataBase.commit()
        DataBase.close()

    except Exception as e:
        return f"Exception!\n\n{e}"



def getDialogList(username):
    try:
        DataBase = mysql.connector.connect(
            host="147.45.138.238",
            port="3306",
            user="gen_user",
            password="Ib&c5<ysBY}l71",
            database="default_db"
        )

        cursor = DataBase.cursor()

#         НАДО ВОЗВРАЩАТЬ СЛОВАРЬ {chatID: userID}


    except Exception as e:
        return f"Exception!\n\n{e}"
