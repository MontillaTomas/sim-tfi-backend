from datetime import datetime


class Dia:
    def __init__(
        self,
        fecha: datetime,
        grado_ataque: float,
        arboles_observados: int,
        dia_humedo: bool = False,
        dia_calido: bool = False,
    ):
        self.fecha = fecha
        self.grado_ataque = grado_ataque
        self.arboles_observados = arboles_observados
        self.dia_humedo = dia_humedo
        self.dia_calido = dia_calido

    def __str__(self):
        return (
            f"Día: {self.fecha}, "
            f"Grado de ataque: {self.grado_ataque}, "
            f"Árboles observados: {self.arboles_observados}, "
            f"Día húmedo: {self.dia_humedo}, "
            f"Día cálido: {self.dia_calido}"
        )
