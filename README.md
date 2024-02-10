# Problem

## Step 1
Write a simple Microservice with 3 services: 1. Accounts 2. Shop 3. Order

### Accounts
    Login -> username, password => token
    Signup -> username, password
    Logout -> delete token
    CheckToken -> token => user
### Shop
    Add to Cart
    Get Items
    Item Detail
    Remove from Cart
    Add Order -> Finalize Cart
    Pay Order
### Order
AddOrder
GetOrders
GetOrderDetail


## Step 2
Dockerize all microservices and Deploy them with docker-compose.

## Step 3
Deploy an nginx with 3 replicas and an HAProxy that load balances between these 3 replicas.
Nginx routes should be like the below:

domain.com/accounts -> accounts_microservice
domain.com/shop -> shop_microservice
domain.com/order -> order_microservice

------
# Solution