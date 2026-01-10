from fastapi import FastAPI
import uvicorn

from apps.app01.user import user
from apps.app02.admin import admin

app = FastAPI()

app.include_router(user, prefix="/user")
app.include_router(admin, prefix="/admin")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)