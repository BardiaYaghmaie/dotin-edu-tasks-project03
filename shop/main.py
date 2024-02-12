from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import asyncpg

app = FastAPI()

# Database connection pool
DATABASE_URL = "postgresql://user:password@postgres/shop"
pool = None

# Models
class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Dependency to get a database connection from the pool
async def get_connection():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(DATABASE_URL)
    async with pool.acquire() as connection:
        yield connection

# Routes
@app.post('/items')
async def create_item(item: Item, connection = Depends(get_connection)):
    try:
        await connection.execute("INSERT INTO items (name, price, quantity) VALUES ($1, $2, $3)",
                                 item.name, item.price, item.quantity)
        return {"message": "Item created successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/items')
async def get_items(connection = Depends(get_connection)):
    records = await connection.fetch("SELECT * FROM items")
    return [{"id": record['id'], "name": record['name'], "price": record['price'], "quantity": record['quantity']} for record in records]

# Start app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
