from datetime import datetime


class Dia:
    def __init__(self, fecha: datetime, grado_ataque: int, arboles_observados: int):
        self.fecha = fecha
        self.grado_ataque = grado_ataque
        self.arboles_observados = arboles_observados

    def __str__(self):
        return (
            f"Día: {self.fecha}, "
            f"Grado de ataque: {self.grado_ataque}, "
            f"Árboles observados: {self.arboles_observados}"
        )
