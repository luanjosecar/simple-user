from pymongo import MongoClient, errors



class Mongo_User():
    DOMAIN = '127.0.0.1'
    PORT = 27017
    MONGOUSER = 'root'
    MONGPWD = 'example'

    def __init__(self):
        print("in init")

    def conect_mong(self):
        try:
            client = MongoClient(
                host = [ str(self.DOMAIN) + ":" + str(self.PORT) ],
                serverSelectionTimeoutMS = 3000, # 3 second timeout
                username = self.MONGOUSER,
                password = self.MONGPWD,
            )
            return client['usuarios']
        except Exception as e: 
            print("Printing Error")
            print(e)
            return None

    def insert_user(self,usuario:str, password:str):
        try:  
            db = self.conect_mong()
            conector = db['users']
            usuario = {"_id": usuario,"password": password}
            conector.insert_one(usuario)
            return {"mesage" : "user Created"}
        except Exception as e: 
            print(e)
            return {"mesage" : "Erro ao Criar Usuario"}

    def find_user(self,username:str):
        db = self.conect_mong()
        conector = db['users']
        usuario = conector.find_one({"_id" : username})
        return usuario

    def update_user(self,username:str, new_value:dict):
        db = self.conect_mong()
        base_value = {"_id":username}
        query = {"$set" : new_value}
        db.users.replace_one(base_value, new_value)