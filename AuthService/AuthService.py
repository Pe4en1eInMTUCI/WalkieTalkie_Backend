from fastapi import FastAPI, Form
import requests
import json

import DataBaseWorker as db
import randomCode as rc

app = FastAPI()


@app.get("/api/voicecode")
def voiceCode(userIP, userPhone):
    response = requests.get(
        f"https://sms.ru/code/call?phone={userPhone}&ip={userIP}&api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD").json()

    if response["status"] == "OK":
        return response["code"]
    else:
        return "Can't call to user!"

@app.get("/api/textcode")
def textCode(userPhone):
    code = rc.random_code()
    response = requests.get(
        f"https://sms.ru/sms/send?api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD&to={userPhone}&msg={code}&json=1").json()

    if response["status"] == "OK":
        return code
    else:
        return "Can't send sms code!"


@app.post("/api/register")
def regUser(phone: str = Form(...), name: str = Form(...), username: str = Form(...), password: str = Form(...)):
    if not db.userExists(phone):
        return db.addUser(phone, name, username, password)

    return 'Error: User exists!'


@app.post("/api/login")
def loginUser(phone: str = Form(...), password: str = Form(...)):
    if db.userExists(phone):
        return db.checkPassword(phone, password)

    return 'Error: User does not exists!'


@app.post("/api/changepassword")
def changePassword(phone: str = Form(...), password: str = Form(...), newPassword: str = Form(...)):
    if db.checkPassword(phone, password):
        db.setPassword(phone, newPassword)
        return "Password changed!"

    return "Error: Wrong password!"


@app.post("/api/getdialogs")
def getDialogs(username: str = Form(...)):
    return db.addDialogList(username)