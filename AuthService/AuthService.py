
from fastapi import FastAPI
import requests
import json


def sendCode(userIP, userPhone):
    response = requests.get(f"https://sms.ru/code/call?phone={userPhone}&ip={userIP}&api_id=2356D300-3BA5-FCFD-7CE5-4F800426C6BD").json()
    print(json.dumps(response))


sendCode("-1", "79778614427")