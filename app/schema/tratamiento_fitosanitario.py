from pydantic import BaseModel


class TratamientoFitosanitarioSchema(BaseModel):
    id: int
    producto: str
    disminucion_grado_ataque: int
    media_inmunidad: int
    desviacion_inmunidad: int
    periodo_carencia: int
    tiempo_entre_aplicaciones: int

    class Config:
        orm_mode = True
