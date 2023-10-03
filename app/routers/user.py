from fastapi import APIRouter
from app.schemas import User

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios = []


@router.post('/Crear_usuario')
def Crear_usuario(user:User):
    usuario = user.dict()
    usuarios.append(usuario)
    return {"respuesta":"Usuario creado correctamente"}


@router.get('/')
def Obtener_usuario():
    return usuarios


@router.get('/{user_id}')
def Obtener_usuario(user_id:int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario":user}
    return {"respuesta":"Usuario no encontrado"}


@router.delete('/{user_id}')
def Eliminar_usuario(user_id:int):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios.pop(index)
            return {"respuesta":"Usuario eliminado Correctamente"}
    return{"respuesta":"Usuario no encontrado"}


@router.put('/{user_id}')
def Actualizar_usuario(user_id:int, updateUser:User):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios[index]["id"] = updateUser.dict()["id"]
            usuarios[index]["nombre"] = updateUser.dict()["nombre"]
            usuarios[index]["apellido"] = updateUser.dict()["apellido"]
            usuarios[index]["telefono"] = updateUser.dict()["telefono"]
            usuarios[index]["direccion"] = updateUser.dict()["direccion"]
            return{"respuesta":"Usuario Actualizado Correctamente"}
    return{"respuesta":"Usuario no encontrado"}


