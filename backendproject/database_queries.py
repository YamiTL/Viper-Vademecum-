from typing import Literal
from pymongo import MongoClient
from bson import json_util
import json

# from main import Pedido

URI = "mongodb+srv://forosypaginas:cySVsfpMe2glBbWC@cluster0.g6tqipp.mongodb.net/"
client = MongoClient(URI)

# Como puedo hacer que get_pedido_by_id acepte pedido_id dinamicos
# Y devuelva el pedido

def connect_to_collection(client: MongoClient):
    db_pedidos = client.get_database("pedidos_backend")
    coleccion_pedidos = db_pedidos["pedidos"]
    return coleccion_pedidos


def get_pedido_by_id(id_del_pedido: str):
    coleccion_pedidos = connect_to_collection(client)
    pedido_from_db: dict[str, str] | None = coleccion_pedidos.find_one(
        {"pedido_id": id_del_pedido}
    )  # type: ignore
    print(pedido_from_db)
    pedido_db_json: dict | None = json.loads(json_util.dumps(pedido_from_db))
    return pedido_db_json

    # pedido_from_db = pedidos_from_db.insert_one(query)


def write_db(query: dict):
    try: 
        coleccion_pedidos = connect_to_collection(client)
        # Query inserting an element that has the name 'Mi'
        pedido = coleccion_pedidos.insert_one(query)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)


def update_db(pedido_actualizado: dict) -> Literal["Okay"]:
    print(pedido_actualizado)
    return "Okay"


db.collection.updateOne(
   { pedido_id: "123" },
   { $set: {customer_id: "miti 2", user_name: "Sali", items: {item_sku: "AR123"}} },
)
