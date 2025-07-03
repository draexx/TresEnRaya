# This is a sample Python script.

# Press Mays+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Tablero:
    def __init__(self):
        # Representación del tablero como una lista de listas para facilitar el acceso por índices.
        # Se mantiene un mapeo de las posiciones amigables a los índices de la lista.
        self.posiciones_mapeadas = {
            "SI": (0, 0), "SC": (0, 1), "SD": (0, 2),
            "CI": (1, 0), "CC": (1, 1), "CD": (1, 2),
            "II": (2, 0), "IC": (2, 1), "ID": (2, 2)
        }
        self.tablero_interno = [[" " for _ in range(3)] for _ in range(3)]

    def imprimir_tablero(self):
        for fila in self.tablero_interno:
            print("|".join(fila))
            print("-+" * 2 + "-")

    def movimiento_valido(self, posicion_str):
        if posicion_str not in self.posiciones_mapeadas:
            return False
        fila, columna = self.posiciones_mapeadas[posicion_str]
        return self.tablero_interno[fila][columna] == " "

    def registro_movimiento(self, posicion_str, tipo):
        if self.movimiento_valido(posicion_str):
            fila, columna = self.posiciones_mapeadas[posicion_str]
            self.tablero_interno[fila][columna] = tipo
            return True # Indica que el movimiento fue exitoso
        return False # Indica que el movimiento no fue válido

    def ganador(self, jugador):
        jugador_tipo = jugador.tipo
        # Comprobación de filas
        for fila in self.tablero_interno:
            if all(s == jugador_tipo for s in fila):
                return True
        # Comprobación de columnas
        for col in range(3):
            if all(self.tablero_interno[fila][col] == jugador_tipo for fila in range(3)):
                return True
        # Comprobación de diagonales
        if all(self.tablero_interno[i][i] == jugador_tipo for i in range(3)):
            return True
        if all(self.tablero_interno[i][2 - i] == jugador_tipo for i in range(3)):
            return True
        return False


class Ficha:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Jugador {self.tipo}"


class Juego:
    def __init__(self):
        self.jugador1 = Ficha("X")
        self.jugador2 = Ficha("O")
        self.tablero = Tablero()

    def imprimir_jugada_valida(self):
        print("""
            SI - Superior Izquierda | SC - Superior Centro | SD - Superior Derecho
            CI
            II - Inferior Izquierdo | IC - Inferior Centro""")

    def imprimiendo_tablero(self):
        self.tablero.imprimir_tablero()

    def cambiar_turno(self, ficha):
        if ficha is self.jugador1:
            return self.jugador2
        else:
            return self.jugador1

    def ganador_juego(self, jugador):
        return self.tablero.ganador(jugador)

    def modificar_tablero(self, posicion, tipo):
        # Intenta registrar el movimiento. Si no es válido, pide nueva entrada hasta que sea válida.
        while not self.tablero.registro_movimiento(posicion, tipo):
            print("Movimiento inválido o la casilla ya está ocupada.")
            # Asegúrate de que las posiciones válidas se muestren claramente si es necesario.
            # self.imprimir_jugada_valida() # Opcional: mostrar de nuevo las posiciones válidas.
            posicion = input(f"Intente de nuevo, {tipo}. ¿Cuál es su movimiento? (ej. SI, CC, ID): ").upper()
        # No es necesario devolver el tablero aquí si la modificación es in-place y exitosa.


def jugar():
    juego = Juego()
    juego.imprimir_jugada_valida()
    jugador_actual = juego.jugador1
    movimientos_realizados = 0
    max_movimientos = 9

    while movimientos_realizados < max_movimientos:
        juego.imprimiendo_tablero()
        print(f"Turno del {jugador_actual}")
        posicion = input("¿Cuál es tu movimiento? (ej. SI, CC, ID): ").upper()

        # La validación de la posición y el registro del movimiento ahora están encapsulados en modificar_tablero
        juego.modificar_tablero(posicion, jugador_actual.tipo)
        movimientos_realizados += 1

        if juego.ganador_juego(jugador_actual):
            juego.imprimiendo_tablero() # Mostrar el tablero final
            print(f"¡Felicidades {jugador_actual}! Has ganado.")
            return # Termina el juego

        if movimientos_realizados == max_movimientos:
            juego.imprimiendo_tablero() # Mostrar el tablero final
            print("El juego ha terminado en empate.")
            return # Termina el juego

        jugador_actual = juego.cambiar_turno(jugador_actual)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jugar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
