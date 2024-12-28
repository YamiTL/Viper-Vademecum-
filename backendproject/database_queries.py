from ast import Dict
from typing import Literal
from pymongo import MongoClient
from bson import json_util
import json
from models import CatalogItem, StatusTypes
# from main import Pedido

URI = "mongodb+srv://forosypaginas:cySVsfpMe2glBbWC@cluster0.g6tqipp.mongodb.net/"
client = MongoClient(URI)


# Orders
def connect_to_pedidos_collection(client: MongoClient):
    db_pedidos = client.get_database("pedidos_backend")
    coleccion_pedidos = db_pedidos["pedidos"]
    return coleccion_pedidos


def get_pedido_by_id(id_del_pedido: str):
    coleccion_pedidos = connect_to_pedidos_collection(client)
    pedido_from_db: dict[str, str] | None = coleccion_pedidos.find_one(
        {"pedido_id": id_del_pedido}
    )  # type: ignore
    print(pedido_from_db)
    # .loads and .dumps below serializes a Mongodb object coming from ddbb to a Fastapi-compatible json
    pedido_db_json: dict | None = json.loads(json_util.dumps(pedido_from_db))  #
    return pedido_db_json


def write_db(query: dict):
    try:
        order_collection = connect_to_pedidos_collection(client)
        pedido = order_collection.insert_one(query)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)


def update_db(updated_id: str, updated_status: StatusTypes) -> Literal["Okay"]:
    coleccion_pedidos = connect_to_pedidos_collection(client)
    query_filter = {"pedido_id": updated_id}
    update_operation = {"$set": {"pedido_status": updated_status}}
    result = coleccion_pedidos.update_one(query_filter, update_operation)
    print(result)
    return "Okay"


# -----------------------------------------------------------------------------------------------


# Catalog
def connect_to_catalog_collection(client: MongoClient):
    db_catalog = client.get_database("pedidos_backend")
    catalog_collection = db_catalog["catalog"]
    return catalog_collection


def receive_catalog_by_sku(catalog_item_sku: str):
    catalog_collection = connect_to_catalog_collection(client)
    catalog_item: dict[str, str] | None = catalog_collection.find_one(
        {"item_sku": catalog_item_sku}
    )
    catalog_db_json: dict | None = json.loads(json_util.dumps(catalog_item))  #
    return catalog_db_json


def write_catalog(catalog_query: dict):
    try:
        catalog_collection = connect_to_catalog_collection(client)
        catalog_add = catalog_collection.insert_one(catalog_query)
    except Exception as e:
        raise Exception("Unable to write on ddbb: ", e)


def update_catalog(updated_catalog_item: CatalogItem) -> None:
    # We defined that we only need an updated catalog item and not an item sku because
    # we can simplify all requirements from this function into just 1 parameter, the Catalog Item
    catalog_connection = connect_to_catalog_collection(client)
    query_filter = {"item_sku": updated_catalog_item.item_sku}
    update_operation = {"$set": {"CatalogItem": updated_catalog_item}}
    result = catalog_connection.update_one(query_filter, update_operation)
    print(result)
