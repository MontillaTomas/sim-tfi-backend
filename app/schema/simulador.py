from datetime import date

from pydantic import BaseModel, Field


class SimuladorInputSchema(BaseModel):
    id_tratamiento: int = Field(..., gt=0)
    hectareas: int = Field(..., gt=0)
    fecha_inicio: date
    fecha_floracion: date
