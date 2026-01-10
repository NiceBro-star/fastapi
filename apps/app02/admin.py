from fastapi import APIRouter

admin = APIRouter()

@admin.post("/login", tags=["管理"])
def login():
    return {"code": 201}