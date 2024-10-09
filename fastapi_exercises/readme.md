# FastApi Exercises

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