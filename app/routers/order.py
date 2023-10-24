from fastapi import APIRouter
from app.schemas import Order
from typing import List, Dict
from fastapi import FastAPI


router = APIRouter(prefix="/process_orders", tags=[""])

@router.post("/Ordenes")
def process_orders(orders: List[dict], criterion: str):
    if not orders:
        return "Error lista vacia debe de llenar la Lista"
    
    # Verificar si hay precios negativos
    positive_prices = []
    negative_prices = []

    for order in orders:
        if order["price"] < 0:
            negative_prices.append(order)
        else:
            positive_prices.append(order)
    if negative_prices:
        error_message = "ERROR: Precio en negativo"
        for order in negative_prices:
            error_message += f"\n ID: {order['id']}, Item: {order['item']}, Quantity: {order['quantity']}, Price: {order['price']}, Status: {order['status']}"
        return error_message

    # Verificar el criterio de filtro
    if criterion not in ["completado", "pendiente", "cancelado", "all"]:
        return "Error: El estado está mal formado"

    # Calcular la suma de precios según el criterio
    total_price = 0
    for order in orders:
        if criterion == "completado":
            total_price = sum(order.get("price", 0) for order in orders if order.get("status") == "completado")
        
        elif criterion == "pendiente":
            total_price = sum(order.get("price", 0) for order in orders if order.get("status") == "pendiente")
        
        elif criterion == "cancelado":
            total_price = sum(order.get("price", 0) for order in orders if order.get("status") == "cancelado")
            
        elif criterion == "all":
            total_price = sum(order.get("price", 0) for order in orders)
        
    return total_price   