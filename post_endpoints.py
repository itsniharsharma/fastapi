from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Users(BaseModel):
    name: str
    age: int

@app.post("/users/")
def create_user(user: Users):
    return {"message":f"User Created Succesfully", "user": user}