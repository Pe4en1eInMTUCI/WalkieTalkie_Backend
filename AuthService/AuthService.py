import json

from flask import Flask, request
import requests

# import DataBaseWorker as db SQLITE DB НЕ ИСПОЛЬЗУЕМ БОЛЬШЕ
import randomCode as rc

import MySQLWorker as db # ИСПОЛЬЗУЕМ MYSQL


app = Flask(__name__)


@app.route("/api/voicecode")
def voiceCode():

    userIP = request.args.get("userIP")
    userPhone = request.args.get("userPhone")

    response = requests.get(
        f"https://sms.ru/code/call?phone={userPhone}&ip={userIP}&api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD").json()

    print(response)

    if response["status"] == "OK":
        return {"code": response["code"]}

    return "Can't call to user!"

@app.route("/api/textcode")
def textCode():

    userPhone = request.args.get('userPhone')

    code = rc.random_code()
    response = requests.get(
        f"https://sms.ru/sms/send?api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD&to={userPhone}&msg={code}&json=1").json()

    if response["status"] == "OK":
        return {"code": code}

    return "Can't send sms code!"


@app.route("/api/register", methods=['POST'])
def regUser():

    phone = request.form.get('phone')
    username = request.form.get('username')
    password = request.form.get('password')

    if not db.phoneExists(phone):
        if not db.usernameExists(username):
            db.addUser(phone, username, password)
            return {"status": "OK"}

        return {"status": "username exists"}

    return {'status': 'phone exists'}


@app.route('/api/possibleToReg', methods=['POST'])
def possibleToReg():
    phone = request.form.get('phone')
    username = request.form.get('username')

    if not db.phoneExists(phone):
        if not db.usernameExists(username):
            return {"status": "OK"}

        return {"status": "username exists"}

    return {'status': 'phone exists'}

@app.route("/api/login", methods=['POST'])
def loginUser():

    phone = request.form.get('phone')
    password = request.form.get('password')

    if db.phoneExists(phone):
        if db.checkPassword(phone, password):
            return {"status": "OK"}

        return {"status": "wrong pass"}

    return {'status': "user not exists"}


# @app.post("/api/changepassword", methods=['POST'])
# def changePassword():
#     if db.checkPassword(phone, password):
#         db.setPassword(phone, newPassword)
#         return "Password changed!"
#    ПОТОМ МБ ДОДЕЛАЕМ
#     return "Error: Wrong password!"



@app.route("/api/getdialogs",  methods=['POST'])
def getDialogs():
    phone = request.form.get('phone')

    username = db.getUsernameByPhone(phone)

    return json.dumps(db.getDialogList(username))


@app.route("/api/getUsernameByPhone",  methods=['POST'])
def usernamebyphone():
    phone = db.getUsernameByPhone(request.form.get('phone'))
    print(phone)
    return {"username": phone}


@app.route('/api/getIDbyUsername', methods=['POST'])
def idbyusername():
    return {'userID': db.getIDbyUsername(request.form.get('username'))}


if __name__ == "__main__":
    app.run(debug=True, port=1232)