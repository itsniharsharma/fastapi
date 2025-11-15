from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"wel to fastapi"}

@app.get("/home")
def read_home():
    return{"message":"this is home page"}