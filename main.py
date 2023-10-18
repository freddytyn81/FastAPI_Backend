from fastapi import FastAPI
from typing import List, Dict
from app.routers import producto
from app.routers import order
import uvicorn

app = FastAPI()

app.include_router(producto.router)
app.include_router(order.router)
