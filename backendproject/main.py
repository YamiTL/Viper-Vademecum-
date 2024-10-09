from fastapi import FastAPI
from pydantic import BaseModel

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


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Necesito hacer una nueva funcion en mi programa que acepte un body
@app.post("/items/")
async def posted_root(mi_pedido: Pedido):
    print(mi_pedido)
    return mi_pedido
