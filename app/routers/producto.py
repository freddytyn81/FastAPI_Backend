from fastapi import FastAPI, APIRouter, HTTPException
from app.schemas import Product
from pydantic import BaseModel
from typing import List


router = APIRouter(prefix="/product", tags=["Productos"])


products = []


@router.post("/Crear_Producto")
def Crear_producto(product: Product):
    for existing_product in products:
        if existing_product.id == product.id:
            return {"message": "El ID del producto ya existe"}

    if product.price <= 0:
        return {"message": "El precio del producto debe ser positivo"}

    if product.status != "completado":
        return {"message": "El estado del producto no es válido"}

    products.append(product)

    return {"message": "Producto agregado exitosamente"}


@router.get("/{product_id}")
def Obtener_Producto(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Producto no encontrado"}


@router.post("/{product_id}")
def eliminar_producto(product_id: int):
    for i, product in enumerate(products):
        if product.id == product_id:
            del products[i]
            return {"message": f"Producto con id {product_id} eliminado"}

    return {"message": f"No se encontró un producto con id {product_id}"}


@router.put("/{product_id}")
def Actualizar_producto(product_id: int, updateProduct: Product):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products[index]["id"] = updateProduct.dict()["id"]
            products[index]["item"] = updateProduct.dict()["item"]
            products[index]["quantity"] = updateProduct.dict()["quantity"]
            products[index]["price"] = updateProduct.dict()["price"]
            products[index]["status"] = updateProduct.dict()["status"]
            return {"respuesta": "Producto Actualizado Correctamente"}
    return {"respuesta": "Producto no encontrado"}

