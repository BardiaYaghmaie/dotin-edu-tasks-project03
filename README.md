# Problem

## Step 1
Write a simple Microservice with 3 services: 1. Accounts 2. Shop 3. Order

### Accounts
    Signup -> username, password
    Login  -> username, password
### Shop
    Add to Cart
    Get Items
    Remove from Cart
### Order
    AddOrder
    GetOrders


## Step 2
Dockerize all microservices and Deploy them with docker-compose.

## Step 3
Deploy an nginx with 3 replicas and an HAProxy that load balances between these 3 replicas.
Nginx routes should be like the below:

localhost:7777/accounts -> accounts_microservice
localhost:7777/shop -> shop_microservice
localhost:7777/order -> order_microservice

------
# Solution

1- Write each service and create a Dockerfile for it
```
# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that the FastAPI application will run on
EXPOSE 80

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
```

2- Install NginxProxyManager