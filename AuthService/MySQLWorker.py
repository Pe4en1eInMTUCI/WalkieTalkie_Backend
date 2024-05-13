import mysql.connector

DataBase = mysql.connector.connect(
    host="147.45.138.238",
    port="3306",
    user="gen_user",
    password="Ib&c5<ysBY}l71",
    database="default_db"
)


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
    except:
        return "Exception"
