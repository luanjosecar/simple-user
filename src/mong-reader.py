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

    def insert_user(usuario):  
        base = 123
        pass