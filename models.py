from datetime import datetime
from pydantic import BaseModel, Field, field_validator

#clientes

class ClienteBase(BaseModel):
    nombre_cliente: str = Field(min_length = 1)
    direccion: str = Field(min_length = 1)

    @field_validator("nombre_cliente", "direccion")
    @classmethod
    def validar_texto(cls, valor):
        valor = valor.strip()
        if not valor:
                raise ValueError("El campo no puede estar vacío")
        return valor

class ClienteCrear(ClienteBase):
        pass

class ClienteActualizar(ClienteBase):
        pass

class Cliente(ClienteBase):
        id_cliente: int
        active: bool


#consumos
class ConsumoCrear(BaseModel):
      id_cliente: int = Field(gt=0)
      consumo_agua: float = Field(ge=0)
      fecha_registro: datetime | None = None

class ConsumoActualizar(BaseModel):
      consumo_agua: float = Field(ge=0)
      fecha_registro: datetime | None = None

class Consumo(BaseModel):
      id_consumo: int
      id_cliente: int
      consumo_agua: float
      fecha_registro: datetime 

class TarifaActualizar(BaseModel):
      tarifa: float = Field(ge=0)

