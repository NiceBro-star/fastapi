from fastapi import APIRouter

user = APIRouter()

@user.post("/login", tags=["登录"])
def login():
    return {"code": 200}