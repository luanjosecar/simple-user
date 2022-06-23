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

def insert_user(nome,senha):  
    base = conect_mong()
    base = base['users']
    usuario = {"_id": nome,"password": senha}
    base.insert_one(usuario)


def find_user(username:str):
    db = conect_mong()
    conector = db['users']
    usuario = conector.find()
    for usr in usuario:
        print(usr)
    print(username)
    print(usuario)
    return usuario

find_user("21323")