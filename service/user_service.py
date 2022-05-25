"""from datetime import timedelta, datetime
from jwt import encode, decode
from jwt import exceptions
from os import getenv
from flask import jsonify, json

def expiration_date(days:int):
    current_date = datetime.now()
    duration_date = current_date + timedelta(days)
    return json.dumps(duration_date)

def create_token(data:dict):
    token = encode(payload={**data, "expiration":expiration_date(3)}, key=getenv("secret"), algorithm="HS256")
    return token

def validate_token(token, output=False):
    try:
        if output is True:
            return decode(token, key=getenv("secret"), algorithms=["HS256"])
        decode(token, key=getenv("secret"), algorithms=["HS256"])

    except exceptions.DecodeError:
        response=jsonify({"Message":"Token Invalido"})
        response.status_code =401
        return response

    except exceptions.ExpiredSignatureError:
        response = jsonify({"Message": "El token ha expirado"})
        response.status_code = 401
        return response"""

from model.user import User
from model.type_user import TypeUser

class UserService:
    def __init__(self):
        self.userList=[]
        self.userList.append(User({"email":"lauralayon@umanizales.edu.co", "password":"1224422"},1,
                                  TypeUser("1","Administrador")))

    def get_users(self):
        list=[]
        for user in self.userList:
            list.append(user.to_user_dto())
        return list

    def validate_user(self, email:str, admi:bool, cant:int):
        count_players=0
        for user in self.userList:
            if user.email == email:
                return True
            if admi and user.type_user.code==1:
                return True

            if user.type_user.code==2:
                count_players+=1

            if admi== False and cant==count_players:
                return True
            return False

    def create_user(self, data):
        admin = False
        if data['type_user']['code'] == 1:
            admin = True
        if self.validate_user(data['email'], admin, 2):
            raise Exception("No cumple las condiciones para adicionar el usuario")

    def login(self, email, password):
        for user in self.userList:
            if email == user.email and password == user.password:
                return user
        return None






