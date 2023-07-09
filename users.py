from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import os

app = FastAPI()


# Iniciar el servidor     
# uvicorn users:app --reload  
#

class User(BaseModel):
    id: int
    name: str


user_list = [
    User(id= 1, name= "Victor"),
    User(id= 2, name= "Rocio"),
    User(id= 3, name= "Gusti")
]      
@app.get("/users")
async def users():
    for obj in user_list:
        print(obj.json())
    return user_list

@app.get("/users/{id}")
async def user(id:int):
    return search_user(id)

@app.get("/users/")
async def user(id:int):
    return search_user(id)

@app.get("/test/{vehicleId}")
async def test(vehicleId:int):
    api_url = os.environ['API_AUTH_URL']
    data = {
        "email":os.environ['API_AUTH_USR'],
        "password":os.environ['API_AUTH_PASS']
    }
    response = requests.post(api_url, json=data)
    api_url = os.environ['API_AUTH_MOCKUP']
    print(api_url)
    data = response.json()

    headers =  {"apikey": 'JDJiJDEwJFhTNmo2b2hzdVBJNU1oN3JtbGY3emVIbUtBNWdFalM2RkV3TGc0aTlQUzhVM1ZtdE9raHph'}
    print(headers)
    response = requests.get(api_url, headers=headers)
    print('RESPONSE => ',response.json())
    email_send_response = send_email(data['token'])

    print(email_send_response.json())
    
    return response.json()

@app.get("/test2")
async def test():
    api_email_url = "https://nodeapi.vjdev.xyz/api/v1/email/send-email"
    headers =  {"apikey": 'JDJiJDEwJFhTNmo2b2hzdVBJNU1oN3JtbGY3emVIbUtBNWdFalM2RkV3TGc0aTlQUzhVM1ZtdE9raHph'}
    data = {
        "to" : "victor.jaramillo@vjdev.xyz",
        "subject": "Email test from Python API"
    }
    response = requests.post(api_email_url, json=data, headers=headers)
    print(os.environ)
    return response.json()     

@app.get("/test3")
async def test():
    response = os.environ['INSTANA_DISABLE'].upper()
    print(os.environ)
    return response

def search_user(id: int):
    users = filter(lambda user: user.id == id , user_list)
    try: 
        return list(users)[0]
    except:
        return {"error": "no se ha encontrado el usuario"}

def send_email(token):
    api_email_url = "https://nodeapi.vjdev.xyz/api/v1/email/send-email"
    headers =  {"x-auth-token": token}
    data = {
        "to" : "victor.jaramillo@vjdev.xyz",
        "subject": "Email test from Python API"
    }
    response = requests.post(api_email_url, json=data, headers=headers)
    return response        


def test():
    streetno = dict(one="Sachin Tendulkar", two="Dravid")
    print(streetno["one"])