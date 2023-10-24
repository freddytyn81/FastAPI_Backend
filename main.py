from fastapi import FastAPI
from typing import List, Dict
from app.routers import order
import uvicorn

app = FastAPI()

app.include_router(order.router)

@app.get('/')
def home():
    return {"Fonoma": "Prueba para Desarrolladores Backend"}