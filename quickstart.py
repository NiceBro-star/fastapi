from fastapi import FastAPI
import uvicorn
import os
from read_response import Read_Response

app = FastAPI()

@app.get("/rest/api/content")
def demo1():
    read_file = Read_Response("response.json")
    return read_file()

if __name__ == "__main__":
  uvicorn.run("quickstart:app", host="0.0.0.0", port=8080, reload=True)