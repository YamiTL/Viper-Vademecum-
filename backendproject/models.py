import datetime
from pydantic import BaseModel
from typing import Literal, Optional

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
    item_price: int  # Este es el precio de venta final/al cliente
    item_description: str
    item_tags: list[str]


# Refleja cada linea/item del carrito
class CartItem(BaseModel):
    item: Item
    quantity: int
    category: str


# Refleja el pedido cuando el cliente hace checkout del carrito
class Pedido(BaseModel):
    pedido_id: str
    creation_date: datetime.datetime
    pedido_status: StatusTypes
    customer_id: str
    user_name: str
    user_address: str
    items: list[CartItem]
    # items: list[tuple[int, Item]]
    payment: list[str]


class CatalogItem(BaseModel):
    """
    #sku id only compulsory when we create a new item, not
    when we put/ update one. So to allow for easier and more
    customer-flexible edition, item_sku needs to be optional.
    """

    item_sku: Optional[str]
    item_image: str
    item_name: str
    item_category: list[str]
    item_description: str
    # Tags para conocer si los items son veggie, vegan, sin TACC, organicos, etc
    item_tags: list[str]


class StockItem(BaseModel):
    item_sku: str
    item_amount: int
