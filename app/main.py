import uvicorn
from fastapi import FastAPI, HTTPException, status

from app.core.simulador import Simulador
from app.repository.repositorio_tratamiento_fitosanitario import (
    RepositorioTratamientoFitosanitario,
)
from app.schema.dia import DiaSchema
from app.schema.simulador import SimuladorInputSchema
from app.schema.tratamiento_fitosanitario import TratamientoFitosanitarioSchema

app = FastAPI()

repositorio = RepositorioTratamientoFitosanitario()
simulador = Simulador()


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


@app.post(
    "/simular",
    response_model=list[DiaSchema],
    status_code=status.HTTP_200_OK,
    tags=["Simulador"],
)
def simular(data: SimuladorInputSchema):
    """
    Endpoint principal para realizar la simulación.
    """
    tratamiento = repositorio.obtener_por_id(data.id_tratamiento)
    if not tratamiento:
        raise HTTPException(status_code=404, detail="Tratamiento no encontrado.")

    try:
        resultados = simulador.simular(
            hectareas=data.hectareas,
            tratamiento=tratamiento,
            fecha_inicio=data.fecha_inicio.strftime("%d/%m/%Y"),
            fecha_floracion=data.fecha_floracion.strftime("%d/%m/%Y"),
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    return resultados


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
