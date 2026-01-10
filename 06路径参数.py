from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/user/{id}")
def get_info(id: int):
    return {"id": id}

@app.get("/username/{username}")
def get_usernmae(username: str):
    return {"username": username}


if __name__ == "__main__":
    uvicorn.run("06路径参数:app", host="0.0.0.0", port=8080, reload=True)