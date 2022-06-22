from pymongo import MongoClient, errors

DOMAIN = '127.0.0.1'
PORT = 27017
MONGOUSER = 'root'
MONGPWD = 'example'


def conect_mong():
    client = MongoClient(
        host = [ str(DOMAIN) + ":" + str(PORT) ],
        serverSelectionTimeoutMS = 3000, # 3 second timeout
        username = MONGOUSER,
        password = MONGPWD,
    )
    return client['usuarios']

def insert_user():  
    base = conect_mong()
    base = base['users']
    usuario = {"_id": "teste","username": "4123123", "password": "241234124124"}
    base.insert_one(usuario)

insert_user()