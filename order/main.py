from fastapi import FastAPI, Depends
import asyncpg

app = FastAPI()

# Database connection pool
DATABASE_URL = "postgresql://user:password@postgres/order"
pool = None

# Dependency to get a database connection from the pool
async def get_connection():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(DATABASE_URL)
    async with pool.acquire() as connection:
        yield connection

# Routes
@app.post('/add-order')
async def add_order(connection = Depends(get_connection)):
    # Dummy implementation, not handling order creation
    return {"message": "Order added successfully"}

@app.get('/orders')
async def get_orders(connection = Depends(get_connection)):
    # Dummy implementation, not retrieving orders from database
    return [{"id": "exampleorderid", "items": [{"item_id": "exampleitemid", "quantity": 2}]}]

@app.get('/orders/{order_id}')
async def get_order_detail(order_id: str, connection = Depends(get_connection)):
    # Dummy implementation, not retrieving order detail from database
    return {"id": order_id, "items": [{"item_id": "exampleitemid", "quantity": 2}]}

# Start app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
