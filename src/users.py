import jwt
from src.mongoReader import Mongo_User
#from src.teste_mongo import insert_user

class Users:
    def __init__(self):
        super().__init__()

    def verify_user(self,username:str, password:str):
        db = Mongo_User()
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
        db = Mongo_User()
        resp = db.insert_user(usuario=username,password=passowrd)
        return resp

    def update_passowrd(self,username:str,password:str, new_passowrd:str):
        db = Mongo_User()
        user = db.find_user(username)
        if(new_passowrd==""):
            return {"Message": "Invalid Passowrd"}

        if(user and user['password'] == password):
            aux = {"password": new_passowrd}
            db.update_user(username,aux)
            return {"Message": "Password Changed"}
        return {"Message": "None"}
        