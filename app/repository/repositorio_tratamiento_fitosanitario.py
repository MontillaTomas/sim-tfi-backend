from app.core.tratamiento_fitosanitario import TratamientoFitosanitario

tratamientos_fitosanitarios = [
    TratamientoFitosanitario(
        id=1,
        producto="Aceite mineral EC 83,03%",
        disminucion_grado_ataque=1,
        media_inmunidad=12,
        desviacion_inmunidad=2,
        periodo_carencia=0,
        tiempo_entre_aplicaciones=30,
    ),
    TratamientoFitosanitario(
        id=2,
        producto="Aceite de soja refinado 85%",
        disminucion_grado_ataque=0,
        media_inmunidad=8,
        desviacion_inmunidad=2,
        periodo_carencia=0,
        tiempo_entre_aplicaciones=14,
    ),
    TratamientoFitosanitario(
        id=3,
        producto="Carbaril WP 85%",
        disminucion_grado_ataque=1,
        media_inmunidad=8,
        desviacion_inmunidad=2,
        periodo_carencia=7,
        tiempo_entre_aplicaciones=14,
    ),
    TratamientoFitosanitario(
        id=4,
        producto="Carbosulfan EC 25%",
        disminucion_grado_ataque=2,
        media_inmunidad=25,
        desviacion_inmunidad=5,
        periodo_carencia=35,
        tiempo_entre_aplicaciones=14,
    ),
    TratamientoFitosanitario(
        id=5,
        producto="Clorpirifós EC 48%",
        disminucion_grado_ataque=2,
        media_inmunidad=22,
        desviacion_inmunidad=2,
        periodo_carencia=21,
        tiempo_entre_aplicaciones=14,
    ),
    TratamientoFitosanitario(
        id=6,
        producto="Dimetoato EC 50%",
        disminucion_grado_ataque=2,
        media_inmunidad=25,
        desviacion_inmunidad=5,
        periodo_carencia=20,
        tiempo_entre_aplicaciones=14,
    ),
    TratamientoFitosanitario(
        id=7,
        producto="Metidation EC 40%",
        disminucion_grado_ataque=3,
        media_inmunidad=33,
        desviacion_inmunidad=2,
        periodo_carencia=30,
        tiempo_entre_aplicaciones=14,
    ),
]


class RepositorioTratamientoFitosanitario:
    def __init__(self):
        self._tratamientos = tratamientos_fitosanitarios

    def obtener_todos(self) -> list[TratamientoFitosanitario]:
        return self._tratamientos

    def obtener_por_id(self, id: int) -> TratamientoFitosanitario | None:
        return next((t for t in self._tratamientos if t.id == id), None)
