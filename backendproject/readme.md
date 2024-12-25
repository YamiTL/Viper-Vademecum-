# Backend Bazaar

## Project Overview
This project is a flexible backend for an ecommerce platform, built using Python, MongoDB, and FastAPI. It provides endpoints for managing a product catalog, orders, cart, and other core functionalities of an online store. 
I intend this project to shine at flexibility, modularity and reusability of components, and careful typing. 

## Technologies Used
Python: The primary programming language.
FastAPI: A high-performance web framework for building APIs.
MongoDB: A NoSQL database for storing product, order, and user data.
PyMongo: A Python driver for MongoDB.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

Installation
Clone the repository:
Bash

git clone https://github.com/your-username/ecommerce-backend.git
Create a virtual environment:
Bash

python -m venv venv
Activate the virtual environment:
Bash

source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows
Install dependencies:
Bash

pip install -r requirements.txt
Set up MongoDB:
Install MongoDB and start the database service.
Create a MongoDB database for the project.
Configure the MongoDB connection string in the config.py file.
Running the Application
Start the application:
Bash

uvicorn app.main:app --reload
API Endpoints
The API provides the following endpoints:

Product Endpoints
Create a product: POST /products
Get a product: GET /products/{product_id}
Get all products: GET /products
Update a product: PUT /products/{product_id}
Delete a product: DELETE /products/{product_id}
Order Endpoints
Create an order: POST /orders
Get an order: GET /orders/{order_id}
Get all orders: GET /orders
Update an order: PUT /orders/{order_id}
Delete an order: DELETE /orders/{order_id}
User Endpoints
Create a user: POST /users
Get a user: GET /users/{user_id}
Get all users: GET /users
Update a user: PUT /users/{user_id}
Delete a user: DELETE /users/{user_id}
Testing

## Useful commands

```Bash
fastapi dev main.py
```

JSON Template for Pedido

{
    "pedido_id": "123",
    "customer_id": "DH283",
    "user_name": "Woolfie",
    "user_address": "General Justo Jose de Urquiza 118",
    "items":[
    
        {
            "item": {
                "item_sku": "JSKGD",
                "item_name": "mimos",
                "item_price": "3746",
                "item_description": "Mi mimi mi MI",
                "vegan": false

            }, 
            "quantity": 9, 
            "category": "Regalos para mitis"
        }
    ],
    "payment": [
        "siendo un pancito", "cheque"
    ]
}