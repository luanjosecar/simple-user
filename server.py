from fastapi import FastAPI
from src.users import Users
from pydantic import BaseModel

app = FastAPI()



class Body(BaseModel):
    user: str
    password: str


@app.get("/heath")
async def root():
    return {"message": "Server Runing"}

@app.post("/login/")
async def user_login(body: Body):
    resp = {"usuario": body.user}
    return resp
