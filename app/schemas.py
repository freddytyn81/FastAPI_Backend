from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id:int
    nombre:str
    apellido:str
    telefono:int
    direccion:Optional[str]
    creacion_user: datetime = datetime.now()