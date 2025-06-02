from datetime import datetime, timedelta

from arbol import Arbol
from dia import Dia
from generador_pseudo_aleatorio import GeneradorLehmer
from tratamiento_fitosanitario import TratamientoFitosanitario


class Simulador:
    def __init__(self):
        self.generador = GeneradorLehmer().obtener_generador()

    def simular(
        self,
        hectareas: int,
        tratamiento: TratamientoFitosanitario,
        fecha_inicio: str,
        fecha_floracion: str,
    ):
        # Validaciones
        if hectareas <= 0:
            raise ValueError("El número de hectáreas debe ser mayor que cero.")

        if not isinstance(tratamiento, TratamientoFitosanitario):
            raise TypeError(
                "El tratamiento debe ser una instancia de TratamientoFitosanitario."
            )

        try:
            fecha_inicio_dt = datetime.strptime(fecha_inicio, "%d/%m/%Y")
            fecha_floracion_dt = datetime.strptime(fecha_floracion, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Las fechas deben estar en el formato 'DD/MM/YYYY'.")

        if fecha_inicio_dt >= fecha_floracion_dt:
            raise ValueError(
                "La fecha de inicio debe ser anterior a la fecha de floración."
            )

        if fecha_inicio_dt.month not in (8, 9):
            raise ValueError("La fecha de inicio debe ser en agosto o septiembre.")

        if not (
            datetime(fecha_floracion_dt.year, 10, 15)
            <= fecha_floracion_dt
            <= datetime(fecha_floracion_dt.year, 11, 15)
        ):
            raise ValueError(
                "La fecha de floración debe estar entre el 15 de octubre y el 15 de noviembre."
            )
        # Inicializo la variable resultados
        resultados = []

        # Calculo días hasta la floración
        dias_hasta_floracion = (fecha_floracion_dt - fecha_inicio_dt).days
        print(f"Días hasta la floración: {dias_hasta_floracion}")

        # Calculo total de árboles y los árboles a observar
        total_arboles = self._calcular_arboles_totales(hectareas)
        print(f"Total de árboles simulados para {hectareas} hectáreas: {total_arboles}")
        arboles_a_observar = [Arbol() for _ in range(int(total_arboles / 10))]

        # Realizo el muestreo para el día inicial y lo agrego a los resultados
        self._realizar_muestreo(arboles_a_observar)
        grado_ataque_inicial = self._calcular_grado_ataque_promedio(arboles_a_observar)
        dia_calido = self._es_dia_calido(fecha_inicio_dt)
        dia_humedo = self._es_dia_humedo(fecha_inicio_dt)
        dia_cero = Dia(
            fecha_inicio_dt,
            grado_ataque_inicial,
            len(arboles_a_observar),
            dia_humedo,
            dia_calido,
        )
        resultados.append(dia_cero)
        print(resultados[0])

        # Simulo la propagación del ataque y la aplicación del tratamiento
        for dia in range(1, dias_hasta_floracion):
            fecha_actual = fecha_inicio_dt + timedelta(days=dia)
            # Obtengo puntos según el día húmedo o cálido y la fecha
            puntos_dia = 0
            dia_calido = self._es_dia_calido(fecha_actual)
            dia_humedo = self._es_dia_humedo(fecha_actual)
            puntos_dia += 1 if dia_calido else 0
            puntos_dia += 1 if dia_humedo else 0
            # Calculo puntos para determinar la evolución del ataque para cada árbol observado
            for arbol in arboles_a_observar:
                puntos = puntos_dia
                # Sumo puntos según la posibilidad de eclosión del 0%, 50% o 100% de los huevos
                puntos += self._obtener_puntos_por_eclosion()
                # Sumo puntos según el grado de ataque del árbol
                puntos += self._obtener_puntos_segun_grado_ataque(arbol)
                # Determino el nuevo grado de ataque del árbol
                self._determinar_nuevo_grado_ataque(puntos, arbol)
            # Calculo el grado de ataque promedio de los árboles observados
            # Y agrego el día a los resultados
            grado_ataque_dia = self._calcular_grado_ataque_promedio(arboles_a_observar)
            dia = Dia(
                fecha_actual,
                grado_ataque_dia,
                len(arboles_a_observar),
                dia_humedo,
                dia_calido,
            )
            print(f"\n{dia}")
            resultados.append(dia)

    def _siguiente_aleatorio(self) -> float:
        """
        Obtiene el siguiente número pseudoaleatorio del generador.
        :return: Un número pseudoaleatorio en el rango [0, 1).
        """
        return next(self.generador)

    def _calcular_arboles_totales(self, hectareas: int) -> int:
        """
        Calcula el número total de árboles en función de las hectáreas.
        :param hectareas: Número de hectáreas.
        :return: Número total de árboles.
        """
        total = 0
        for i in range(hectareas):
            u = self._siguiente_aleatorio()
            arboles = int(300 + 120 * u)
            print(f"Hectárea {i + 1}: u = {u:.5f} → árboles = {arboles}")
            total += arboles
        return total

    def _realizar_muestreo(self, arboles: list[Arbol]) -> None:
        """
        Realiza un muestreo de los árboles para observar su estado.
        :param arboles: Lista de árboles a observar.
        :return: Lista de días con el grado de ataque y árboles observados.
        """
        for i in range(len(arboles)):
            u = self._siguiente_aleatorio()
            if u <= 0.2:
                grado_ataque = 0
            elif u <= 0.4:
                grado_ataque = 1
            elif u <= 0.6:
                grado_ataque = 2
            elif u <= 0.8:
                grado_ataque = 3
            else:
                grado_ataque = 4
            print(f"Árbol observado: u = {u:.5f} → grado de ataque = {grado_ataque}")
            arboles[i].grado_ataque = grado_ataque

    def _calcular_grado_ataque_promedio(self, arboles: list[Arbol]) -> int:
        """
        Calcula el grado de ataque promedio de los árboles observados.
        :param arboles: Lista de árboles observados.
        :return: Grado de ataque promedio.
        """
        total_grado = sum(arbol.grado_ataque for arbol in arboles)
        return total_grado / len(arboles) if arboles else 0

    def _obtener_puntos_por_eclosion(self) -> int:
        """
        Determina los puntos por eclosión de huevos.
        :return: 0, 1 o 2 puntos según la probabilidad.
        """
        u = self._siguiente_aleatorio()
        if u <= 1 / 3:
            return 0
        elif u <= 2 / 3:
            return 1
        else:
            return 2

    def _es_dia_humedo(self, fecha: datetime) -> bool:
        """
        Verifica si el día es húmedo según la fecha.
        :param fecha: Fecha a verificar.
        :return: True si es un día húmedo, False en caso contrario.
        """
        u = self._siguiente_aleatorio()
        if fecha.month == 8:
            return u <= 0.35
        else:
            return u <= 0.38

    def _es_dia_calido(self, fecha: datetime) -> bool:
        """
        Verifica si el día es cálido según la fecha.
        :param fecha: Fecha a verificar.
        :return: True si es un día cálido, False en caso contrario.
        """
        u = self._siguiente_aleatorio()
        if fecha.month == 8:
            return u <= 0.25
        else:
            return u <= 0.8

    def _obtener_puntos_segun_grado_ataque(self, arbol: Arbol) -> int:
        """
        Obtiene puntos según el grado de ataque del árbol.
        :param arbol: Árbol a evaluar.
        :return: Puntos según el grado de ataque.
        """
        if arbol.grado_ataque == 0:
            return 0
        elif arbol.grado_ataque == 1:
            return 1
        elif arbol.grado_ataque == 2:
            return 2
        elif arbol.grado_ataque == 3:
            return 3
        else:
            return 4

    def _determinar_nuevo_grado_ataque(self, puntos: int, arbol: Arbol) -> None:
        """
        Calcula el nuevo grado de ataque basado en los puntos obtenidos. Si el grado de ataque es menor a 4, se puede incrementar.
        :param puntos: Puntos obtenidos.
        :return: Nuevo grado de ataque.
        """
        u = self._siguiente_aleatorio()
        if arbol.grado_ataque < 4:
            if puntos <= 2:
                if u <= 0.05:
                    arbol.grado_ataque += 1
                elif puntos <= 4:
                    if u <= 0.1:
                        arbol.grado_ataque += 1
            elif puntos <= 6:
                if u <= 0.2:
                    arbol.grado_ataque += 1
            elif puntos <= 8:
                if u <= 0.5:
                    arbol.grado_ataque += 1


if __name__ == "__main__":
    tratamiento = TratamientoFitosanitario(
        id=6,
        producto="Dimetoato EC 50%",
        disminucion_grado_ataque=2,
        media_inmunidad=25,
        desviacion_inmunidad=5,
        periodo_carencia=20,
        tiempo_entre_aplicaciones=14,
    )
    simulador = Simulador()

    try:
        simulador.simular(
            hectareas=3,
            tratamiento=tratamiento,
            fecha_inicio="20/08/2025",
            fecha_floracion="30/10/2025",
        )
    except Exception as e:
        print(f"Error en la simulación: {e}")
