from fastapi import FastAPI, HTTPException
from database_queries import update_db, write_db
from database_queries import get_pedido_by_id
from models import Pedido, StatusTypes

app = FastAPI()


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
async def updated_root(pedido_id: str, pedido_status: StatusTypes):
    result = update_db(pedido_id, pedido_status)
    print(result)
    return result
