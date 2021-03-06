from fastapi import FastAPI
from src.users import Users
from pydantic import BaseModel

app = FastAPI()


usr = Users()

class Body(BaseModel):
    user: str
    password: str
    new_passowrd :str = ""


@app.get("/heath")
async def root():
    return {"message": "Server Runing"}

@app.post("/login/")
async def user_login(body: Body):

    resp = usr.verify_user(body.user, body.password)
    return resp


@app.post("/cadastro/")
async def register_user(body: Body):
    resp = usr.create_user(body.user, body.password)
    return resp

@app.post("/modify/")
async def register_user(body: Body):
    resp = usr.update_passowrd(body.user, body.password, body.new_passowrd)
    return resp