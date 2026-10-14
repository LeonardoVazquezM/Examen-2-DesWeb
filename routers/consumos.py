from datetime import datetime
from fastapi import APIRouter, HTTPException
from models import ConsumoCrear, ConsumoActualizar
import storage

router = APIRouter(
    prefix="/v1/api/consumos",
    tags=["Consumos"]
)

# Acceder a las listas:
# storage.clientes
# storage.consumos

@router.get("/")
def obtener_consumos():
    return {
        "success": True,
        "total_consumos": len(storage.consumos),
        "consumos": storage.consumos
    }

@router.post("/", status_code=201)
def registrar_consumo(consumo: ConsumoCrear):
    cliente_encontrado = None
    for c in storage.clientes:
        if c["id_cliente"] == consumo.id_cliente:
            cliente_encontrado = c
            break
            
    if not cliente_encontrado:
        raise HTTPException(status_code=404, detail="El cliente no existe")
        
    if not cliente_encontrado["active"]:
        raise HTTPException(status_code=400, detail="No se pueden registrar consumos a clientes inactivos")
        
    fecha_final = consumo.fecha_registro
    if fecha_final is None:
        fecha_final = datetime.now()
        
    nuevo_consumo = {
        "id_consumo": storage.siguiente_id_consumo,
        "id_cliente": consumo.id_cliente,
        "consumo_agua": consumo.consumo_agua,
        "fecha_registro": fecha_final
    }
    
    storage.consumos.append(nuevo_consumo)
    storage.siguiente_id_consumo += 1
    
    return {
        "success": True,
        "message": "Consumo registrado correctamente",
        "consumo": nuevo_consumo
    }

@router.put("/{id_consumo}")
def actualizar_consumo(id_consumo: int, datos: ConsumoActualizar):
    consumo_encontrado = None
    for consumo in storage.consumos:
        if consumo["id_consumo"] == id_consumo:
            consumo_encontrado = consumo
            break
            
    if not consumo_encontrado:
        raise HTTPException(status_code=404, detail="El consumo no existe")
        
    cliente_encontrado = None
    for c in storage.clientes:
        if c["id_cliente"] == consumo_encontrado["id_cliente"]:
            cliente_encontrado = c
            break
            
    if cliente_encontrado and not cliente_encontrado["active"]:
        raise HTTPException(status_code=400, detail="No se puede actualizar el consumo porque el cliente está inactivo")
        
    consumo_encontrado["consumo_agua"] = datos.consumo_agua
    
    return {
        "success": True,
        "message": "Consumo actualizado correctamente",
        "consumo": consumo_encontrado
    }