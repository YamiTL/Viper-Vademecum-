from typing import Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database_queries import update_db, write_db
from database_queries import get_pedido_by_id

# Possible states for Orders
StatusTypes = (
    Literal["Created"]
    | Literal["Confirmed"]
    | Literal["ReadyForCustomer"]
    | Literal["PickedUp"]
    | Literal["Closed"]
)

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
    pedido_status: StatusTypes
    customer_id: str
    user_name: str
    user_address: str
    items: list[CartItem]
    # items: list[tuple[int, Item]]
    payment: list[str]


# Hay que cargar pedidos en la base que tengan sus estados
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


@app.put("/pedidos_backend/")
async def updated_root(pedido_status: StatusTypes):
    return update_db({})
