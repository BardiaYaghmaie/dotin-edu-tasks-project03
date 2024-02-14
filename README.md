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

2- Configure Nginx 
```pr03.conf
server {
    listen 0.0.0.0:7777;
    server_name localhost;

    location /account {
        proxy_pass http://199.20.45.10:80;  
    }

    location /shop {
        proxy_pass  http://199.20.45.11:80;  
    }

    location /order {
        proxy_pass  http://199.20.45.12:80; 
    }
}


```
```Dockerfile
# Dockerfile for Nginx
FROM nginx:alpine

# Copy your custom Nginx configuration file into the container
COPY pr03.conf /etc/nginx/conf.d/default.conf

```

3- Write docker compose file and configure networking.
```docker-compose.yml
version: '3'
services:
  accounts:
    build:
      context: ./account
    ports:
      - "8000:80"
    container_name: account
    hostname: account
    networks:
      pr03:
        ipv4_address: 199.20.45.10
  shop:
    build:
      context: ./shop
    ports:
      - "8001:80"
    container_name: shop
    hostname: shop
    networks:
      pr03:
        ipv4_address: 199.20.45.11
  order:
    build:
      context: ./order
    ports:
      - "8002:80"
    container_name: order
    hostname: order
    networks:
      pr03:
        ipv4_address: 199.20.45.12
  nginx:
    build:
      context: ./nginx
    ports:
      - "7777:7777"
    networks:
      - pr03

networks:
  pr03:
    driver: bridge
    ipam:
     config:
       - subnet: 199.20.45.0/24
         gateway: 199.20.45.1
```