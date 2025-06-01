class TratamientoFitosanitario:
    def __init__(
        self,
        id: int,
        producto: str,
        disminucion_grado_ataque: int,
        media_inmunidad: int,
        desviacion_inmunidad: int,
        periodo_carencia: int,
        tiempo_entre_aplicaciones: int,
    ):
        self.id = id
        self.producto = producto
        self.disminucion_grado_ataque = disminucion_grado_ataque
        self.media_inmunidad = media_inmunidad
        self.desviacion_inmunidad = desviacion_inmunidad
        self.periodo_carencia = periodo_carencia
        self.tiempo_entre_aplicaciones = tiempo_entre_aplicaciones

    def __str__(self):
        return (
            f"TratamientoFitosanitario(id={self.id}, producto={self.producto}, "
            f"disminucion_grado_ataque={self.disminucion_grado_ataque}, "
            f"media_inmunidad={self.media_inmunidad}, "
            f"desviacion_inmunidad={self.desviacion_inmunidad}, "
            f"periodo_carencia={self.periodo_carencia}, "
            f"tiempo_entre_aplicaciones={self.tiempo_entre_aplicaciones})"
        )
