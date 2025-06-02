from datetime import datetime

from pydantic import BaseModel


class DiaSchema(BaseModel):
    fecha: datetime
    grado_ataque: float
    arboles_observados: int
    dia_humedo: bool = False
    dia_calido: bool = False
    aplicacion_tratamiento_fitosanitario: bool = False

    class Config:
        orm_mode = True
