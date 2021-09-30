from fastapi import FastAPI
import uvicorn
from functions import *

# http://localhost:5003/docs
# http://localhost:5003/redoc

app = FastAPI()

@app.get("/name/{name}")
def search_name_API(name: str):
    return search_name(name)

if __name__ == "__main__":
    uvicorn.run("app:app", host='127.0.0.1', reload=True, port=5003)
    