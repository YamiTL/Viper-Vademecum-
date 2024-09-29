from pydantic import BaseModel


class Pedido(BaseModel):
    pedido_id: str
    user_name: str
    user_address: str
    items: list
    payment: list


mi_pedido = {
    "pedido_id": "1",
    "user_name": "Woolfie",
    "user_address": "General Urquiza",
    "items": ["Pollito", "Venganza"],
    "payment": ["mlem"],
}
mi_pedido_validado = Pedido.model_validate(mi_pedido)

print(mi_pedido_validado)
