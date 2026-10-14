from fastapi import APIRouter, HTTPException
from models import TarifaActualizar
import storage

router = APIRouter(
    prefix="/v1/api/tarifa",
    tags=["Tarifas"]
)

# Consultar: storage.tarifa_actual
# Actualizar: storage.tarifa_actual = nueva_tarifa

@router.get("/")
def obtener_tarifa():
    return {
        "success": True,
        "tarifa_actual": storage.tarifa_actual
    }

# Actualiza tarifa global
@router.put("/")
def actualizar_tarifa(datos: TarifaActualizar):
    
    storage.tarifa_actual = datos.tarifa
    return {
        "success": True,
        "message": "Tarifa actualizada correctamente",
        "nueva_tarifa": storage.tarifa_actual
    }