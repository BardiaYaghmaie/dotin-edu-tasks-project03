# accounts_microservice/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database (for demonstration purposes)
users_db = {}

class UserSignup(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@app.post("/AddToCart")
def signup(user_data: UserSignup):
    username = user_data.username
    if username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[username] = user_data.password
    return {"message": f"User {username} registered successfully"}

@app.post("/GetItems")
def login(user_data: UserLogin):
    username = user_data.username
    password = user_data.password
    stored_password = users_db.get(username)
    if stored_password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": f"Welcome back, {username}"}
