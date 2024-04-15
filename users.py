from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_db = [User(name ="Name1", surname = "Surname1", url = "url1", age = 20),
            User(name = "Name2", surname = "Surname2", url = "url2", age = 21),
            User(name = "Name3", surname = "Surname3", url = "url3", age = 22)]

@app.get("/users")
async def users():
    return users_db