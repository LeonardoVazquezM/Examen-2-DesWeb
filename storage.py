from datetime import datetime


# Almacenamiento de clientes
clientes = [ 
    {
    "id_cliente": 1,
    "nombre_cliente": "Juan Perez",
    "direccion": "Monterrey, Nuevo Leon",
    "active": True
    }
  
]

# Almacenamiento de consumos
consumos = [
    {
    "id_consumo": 1,
    "id_cliente": 1,
    "consumo_agua": 120.5,
    "fecha_registro": "2026-10-12T14:30:00"
    }
]

# Tarifa inicial del agua
tarifa_actual = 0.50

siguiente_id_cliente = 2
siguiente_id_consumo = 2
