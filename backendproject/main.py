from os import path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database_queries import write_db
from database_queries import get_pedido_by_id

app = FastAPI()


# Refleja cada producto unico del catalogo/stock
class Item(BaseModel):
    item_sku: str
    item_name: str
    item_price: int
    item_description: str
    vegan: bool


# Refleja cada linea/item del carrito
class CartItem(BaseModel):
    item: Item
    quantity: int
    category: str


# Refleja el pedido cuando el cliente hace checkout del carrito
class Pedido(BaseModel):
    pedido_id: str
    customer_id: str
    user_name: str
    user_address: str
    items: list[CartItem]
    # items: list[tuple[int, Item]]
    payment: list[str]


item_1 = Item.model_validate(
    {
        "item_sku": "AR322F",
        "item_name": "pollito",
        "item_price": 3746,
        "item_description": "Mi mimi mi MI",
        "vegan": False,
    }
)

cart_item = CartItem.model_validate(
    {"item": item_1, "quantity": 1, "category": "alimento"}
)

mi_pedido = {
    "pedido_id": "1",
    "customer_id": "miti 1",
    "user_name": "Woolfie",
    "user_address": "General Urquiza",
    "items": [cart_item],
    # "items": [(1, item_1)],
    "payment": ["mlem"],
}
mi_pedido_validado = Pedido.model_validate(mi_pedido)


@app.get(path="/pedidos_backend/{pedido_id}")
async def received_root(pedido_id: str):
    pedido_recibido = get_pedido_by_id(pedido_id)
    if pedido_recibido is None:
        raise HTTPException(
            status_code=404,
            detail="Tu pedido no existe en nuestros registros. Verifica el numero.",
        )
    return pedido_recibido


# Necesito hacer una nueva funcion en mi programa que acepte un body
@app.post("/pedidos_backend/")
async def posted_root(mi_pedido: Pedido):
    pedido_guardado = write_db(mi_pedido.model_dump())
    return mi_pedido


# write_db(mi_pedido_validado.model_dump())
