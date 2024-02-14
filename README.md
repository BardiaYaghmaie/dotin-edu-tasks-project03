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