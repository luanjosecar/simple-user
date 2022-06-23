import jwt
from src.mongoReader import Mongo_reader
#from src.teste_mongo import insert_user

class Users:
    def __init__(self):
        super().__init__()

    def verify_user(self,username:str, password:str):
        db = Mongo_reader()
        user = db.find_user(username)
        if(user):
            if(user['password'] == password):
                encoded_jwt = jwt.encode({"username": username}, "secret", algorithm="HS256")
                return {"Message": "User Found", "Token": "Bearer "+str(encoded_jwt)}
            else:
                return {"Message": "Wrong Password"}
        else:
            return {"Message": "User not Found"}
    def create_user(self,username:str, passowrd:str):
        db = Mongo_reader()
        resp = db.insert_user(usuario=username,password=passowrd)
        return resp