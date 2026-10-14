from fastapi import APIRouter, HTTPException
from models import ClienteCrear, ClienteActualizar
import storage

router = APIRouter(
    prefix="/v1/api/clientes",
    tags=["Clientes"]
)

@router.get("")
def obtener_clientes():
    return {
        "success": True,
        "total_clientes": len(storage.clientes),
        "clientes": storage.clientes
    }

@router.post("", status_code=201)
def crear_cliente(cliente: ClienteCrear):
    nuevo_cliente = {
        "id_cliente": storage.siguiente_id_cliente,
        "nombre_cliente": cliente.nombre_cliente,
        "direccion": cliente.direccion,
        "active": True
    }
    storage.clientes.append(nuevo_cliente)
    storage.siguiente_id_cliente += 1

    return {
        "success": True,
        "message": "Cliente creado exitosamente",
        "cliente": nuevo_cliente
    }

@router.put("/{id_cliente}")
def actualizar_cliente(id_cliente: int, datos: ClienteActualizar):
    for cliente in storage.clientes:
        if cliente["id_cliente"] == id_cliente:
            cliente["nombre_cliente"] = datos.nombre_cliente
            cliente["direccion"] = datos.direccion

            return {
                "success": True,
                "message": "Cliente actualizado exitosamente",
                "cliente": cliente
            }
    raise HTTPException(
        status_code= 404,
        detail = "Cliente no encontrado"
    )

@router.delete("/{id_cliente}")
def desactivar_cliente(id_cliente: int):
    for cliente in storage.clientes:
        if cliente["id_cliente"] == id_cliente:
            cliente["active"] = False
            return {
                "success": True,
                "message": "Cliente desactivado correctamente.",
                "cliente": cliente
            }
    raise HTTPException(
        status_code = 404,
        detail="Cliente no encontrado"
    )
