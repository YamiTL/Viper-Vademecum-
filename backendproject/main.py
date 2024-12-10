from fastapi import FastAPI, HTTPException
from database_queries import update_db, write_db, write_catalog, receive_catalog_by_sku
from database_queries import get_pedido_by_id
from models import CatalogItem, Pedido, StatusTypes, CatalogItem

app = FastAPI()


# Funcion para obtener pedidos de mi ddbb
@app.get(path="/pedidos_backend/order/{pedido_id}")
async def received_order(pedido_id: str):
    received_order = get_pedido_by_id(pedido_id)
    if received_order is None:
        raise HTTPException(
            status_code=404,
            detail="Tu pedido no existe en nuestros registros. Verifica el numero.",
        )
    return received_order


# Funcion para cargar pedidos en mi ddbb
@app.post("/pedidos_backend/")
async def posted_order(mi_pedido: Pedido):
    pedido_guardado = write_db(mi_pedido.model_dump())
    return mi_pedido


# Funcion para editar/actualizar pedidos de mi ddbb
@app.put("/pedidos_backend/")
async def updated_order(pedido_id: str, pedido_status: StatusTypes):
    result = update_db(pedido_id, pedido_status)
    print(result)
    return result


# Funcion para obtener un Catalog item a mi ddbb
@app.get("/pedidos_backend/catalog/{item_sku}")
async def received_catalog(item_sku: str):
    receive_catalog = receive_catalog_by_sku(item_sku)
    if receive_catalog is None:
        raise HTTPException(
            status_code=404,
            detail="Ése item no existe en nuestro catálogo. Verificá el nombre o SKU.",
        )
    return item_sku


# Funcion para agregar un Catalog item a mi ddbb
@app.post("/pedidos_backend/catalog")
async def posted_catalog(catalog_item: CatalogItem):
    if catalog_item.item_sku is None:
        raise HTTPException(
            status_code=422,
            detail="El SKU es obligatorio para la creación de un item en catálogo.",
        )
    post_catalog = write_catalog(catalog_item.model_dump())
    # Every time I need to add a Python dictionary to Pymongo,
    # I need to convert the Pydantic object into a Pymongo object. Thus, model_dump.
    return catalog_item


# Funcion para editar un Catalog item a mi ddbb
@app.put("/pedidos_backend/catalog")
async def updated_catalog(catalog_item: CatalogItem) -> CatalogItem:
    if catalog_item.item_sku is not None:
        raise HTTPException(
            status_code=422,
            detail="Los SKU de los productos de catalogo no son modificables. Para ingresar un nuevo SKU, crea un nuevo item en Catalogo.",
        )
    return catalog_item
