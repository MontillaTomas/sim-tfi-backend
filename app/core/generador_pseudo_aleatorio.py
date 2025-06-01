from abc import ABC, abstractmethod


class GeneradorPseudoaleatorio(ABC):
    @abstractmethod
    def obtener_generador(self):
        """
        Generador infinito que produce números pseudoaleatorios en [0, 1).
        :yield: Un número pseudoaleatorio.
        """
        pass


class GeneradorLehmer(GeneradorPseudoaleatorio):
    def __init__(self, semilla: int = 35451, t: int = 73):
        self.n_actual = semilla
        self.t = t
        self.k = len(str(t))  # Número de dígitos de t

    def obtener_generador(self):
        """
        Generador infinito que produce números pseudoaleatorios usando el método de Lehmer por dígitos.
        :yield: Un número pseudoaleatorio en el rango [0, 1).
        """
        while True:
            producto = self.n_actual * self.t
            producto_str = str(producto).zfill(len(str(self.n_actual)))
            primeros_k_digitos = producto_str[: self.k]
            resto_derecha = producto_str[self.k :]

            if resto_derecha == "":
                resto_derecha = "0"

            self.n_actual = abs(int(resto_derecha) - int(primeros_k_digitos))
            u_i = self.n_actual / (10 ** len(str(self.n_actual)))
            yield u_i


def main():
    print("Generador Pseudoaleatorio - Método de Lehmer")
    semilla = int(input("Ingrese la semilla (n₀) [default=35451]: ") or 35451)
    t = int(input("Ingrese el valor de t [default=73]: ") or 73)

    generador = GeneradorLehmer(semilla, t)
    generador_iter = generador.obtener_generador()

    print("\nPresione Enter para generar un número pseudoaleatorio.")
    print("Escriba 'q' o 'Q' para salir.\n")

    contador = 1
    while True:
        user_input = input(f"[{contador}] > ")
        if user_input.lower() == "q":
            print("Saliendo del generador.")
            break
        numero = next(generador_iter)
        print(f"{contador}: {numero:.5f}")
        contador += 1


if __name__ == "__main__":
    main()
