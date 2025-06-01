from fastapi import FastAPI, status

from app.repository.repositorio_tratamiento_fitosanitario import (
    RepositorioTratamientoFitosanitario,
)
from app.schema.tratamiento_fitosanitario import TratamientoFitosanitarioSchema

app = FastAPI()

repositorio = RepositorioTratamientoFitosanitario()


@app.get(
    "/tratamientos-sanitarios",
    response_model=list[TratamientoFitosanitarioSchema],
    status_code=status.HTTP_200_OK,
    tags=["Tratamientos Sanitarios"],
)
def obtener_tratamientos_sanitarios():
    """
    Endpoint para obtener todos los tratamientos fitosanitarios.
    """
    return repositorio.obtener_todos()
