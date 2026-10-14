from fastapi import APIRouter
import storage

router = APIRouter(
    prefix="/v1/api/reportes",
    tags=["Reportes"]
)


@router.get("/")
def obtener_reporte_consumos():
    reporte = []
    
    for consumo in storage.consumos:
        total_pagar = consumo["consumo_agua"] * storage.tarifa_actual
        
        consumo_con_total = consumo.copy()
        consumo_con_total["total_pagar"] = total_pagar
        reporte.append(consumo_con_total)
        
    return {
        "success": True,
        "tarifa_aplicada": storage.tarifa_actual,
        "total_registros": len(reporte),
        "reporte": reporte
    }