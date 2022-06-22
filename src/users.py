import jwt
from mongoReader import Mongo_reader

class Users(Mongo_reader):
    def verify_user(username:str, password:str):
        encoded_jwt = jwt.encode({"username": username}, "secret", algorithm="HS256")
        return {"Message": "User Found", "Token": "Bearer "+str(encoded_jwt)}
        
    def create_user(username:str, passowrd:str):
        resp = insert_user(username,passowrd)
        return resp