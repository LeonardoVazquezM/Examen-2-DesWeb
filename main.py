from fastapi import FastAPI
from routers.clientes import router as clientes_router
from routers.consumos import router as consumos_router
from routers.tarifas import router as tarifas_router
from routers.reportes import router as reportes_router

app = FastAPI(
    title = "Api Agua y drenaje :)",
    description = "API REST para administras clientres y consumos",
    version = "0.0.1"
)

app.include_router(clientes_router)
app.include_router(consumos_router)
app.include_router(tarifas_router)
app.include_router(reportes_router)

@app.get("/")
def inicio():
    return {
        "success": True,
        "message": "API Agua y drenaje"
    
    }