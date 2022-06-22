from pymongo import MongoClient, errors

DOMAIN = ''
PORT = 27017
MONGOUSER = 'root'
MONGPWD = 'example'

class Mongo_reader():
    def conect_mong():
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = MONGOUSER,
            password = MONGPWD,
        )
        return client['usuarios']

    def insert_user(usuario:str, password:str):
        try:  
            conector = conect_mong()
            conector = base['users']
            usuario = {"_id": usuario,"password": password}
            conector.insert_one(usuario)
            return {"mesage" : "user Created"}
        except:
            return {"mesage" : "Erro ao Criar Usuario"}

    def find_user(username:str):
        db = conect_mong()
        usuario = db.sensor.find({"_id" : username})
        return usuario