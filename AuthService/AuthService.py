
from fastapi import FastAPI, Form
import requests
import json

import DataBaseWorker as db


app = FastAPI()


@app.get("/api")
def default():
    return "WalkieTalkie AuthService is working!"


@app.get("/api/sendcode")
def sendCode(userIP, userPhone):
    response = requests.get(f"https://sms.ru/code/call?phone={userPhone}&ip={userIP}&api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD").json()
    return response["code"]


@app.post("/api/register")
def regUser(phone: str = Form(), username: str = Form(...), password: str = Form(...)):
    if not db.userExists(username):
        return db.addUser(phone, username, password)
    else:
        return 'Error: User exists!'




@app.post("/api/login")
def loginUser():
    pass




