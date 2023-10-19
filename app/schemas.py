from pydantic import BaseModel
from typing import List, Any


class Product(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str

