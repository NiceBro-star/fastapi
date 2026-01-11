from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/jobs")
def get_job(name, age, edu):
    return {"name": name, "age": age, "edu": edu}

if __name__ == "__main__":
    uvicorn.run("07查询参数:app", port=8080, reload=True)