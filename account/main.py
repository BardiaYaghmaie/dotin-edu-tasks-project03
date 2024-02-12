from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import asyncpg

app = FastAPI()

# Database connection pool
DATABASE_URL = "postgresql://user:password@postgres/accounts"
pool = None

# Models
class User(BaseModel):
    username: str
    password: str

# Dependency to get a database connection from the pool
async def get_connection():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(DATABASE_URL)
    async with pool.acquire() as connection:
        yield connection

# Routes
@app.post('/signup')
async def signup(user: User, connection = Depends(get_connection)):
    try:
        await connection.execute("INSERT INTO users (username, password) VALUES ($1, $2)", user.username, user.password)
        return {"message": "User created successfully"}
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Username already exists")

@app.post('/login')
async def login(user: User, connection = Depends(get_connection)):
    record = await connection.fetchrow("SELECT password FROM users WHERE username = $1", user.username)
    if record is None or record['password'] != user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"token": "exampletoken"}  # Generate and return token

# Start app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
