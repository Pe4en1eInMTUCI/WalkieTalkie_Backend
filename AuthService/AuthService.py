import json

from flask import Flask, request
import requests
from pydantic import BaseModel

import DataBaseWorker as db
import randomCode as rc


app = Flask(__name__)


@app.route("/api/voicecode")
def voiceCode(userIP, userPhone):
    response = requests.get(
        f"https://sms.ru/code/call?phone={userPhone}&ip={userIP}&api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD").json()

    if response["status"] == "OK":
        return response["code"]
    else:
        return "Can't call to user!"

@app.route("/api/textcode")
def textCode(userPhone):
    code = rc.random_code()
    response = requests.get(
        f"https://sms.ru/sms/send?api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD&to={userPhone}&msg={code}&json=1").json()

    if response["status"] == "OK":
        return code
    else:
        return "Can't send sms code!"


@app.route("/api/register", methods=['POST'])
def regUser():

    phone = request.form.get('phone')
    name = request.form.get('phone')
    username = request.form.get('phone')
    password = request.form.get('phone')

    if not db.userExists(phone):
        return db.addUser(phone, name, username, password)

    return 'Error: User exists!'


@app.route("/api/login", methods=['POST'])
def loginUser():

    phone = request.form.get('phone')
    password = request.form.get('password')

    if db.userExists(phone):
        if db.checkPassword(phone, password):
            return {"status": "OK"}

        return {"status": "wrong pass"}

    return {'status': "user not exists"}


# @app.post("/api/changepassword", methods=['POST'])
# def changePassword():
#     if db.checkPassword(phone, password):
#         db.setPassword(phone, newPassword)
#         return "Password changed!"
#
#     return "Error: Wrong password!"



@app.route("/api/getdialogs",  methods=['POST'])
def getDialogs():
    username = request.form.get('username')

    return json.dumps(db.getDialogs(username))


if __name__ == "__main__":
    app.run(debug=True, port=1232)