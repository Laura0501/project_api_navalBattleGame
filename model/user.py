from model.type_user import TypeUser
from .user_dto import UserDTO

class User:
    def __init__(self, data, id:int, type_user:TypeUser):
        if 'email' in data and 'password' in data:
            self.email=data['email']
            self.password=data['password']
            self.type_user=type_user
            self.id=id

        else:
            raise Exception("Los atributos estan incompletos para crear el usuario")


    def to_user_dto(self):
        return UserDTO(self.email,self.type_user.description)