from pydantic import BaseModel
from typing import Literal

# Possible states for Orders
StatusTypes = (
    Literal["Created"]
    | Literal["Confirmed"]
    | Literal["ReadyForCustomer"]
    | Literal["PickedUp"]
    | Literal["Closed"]
)


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
