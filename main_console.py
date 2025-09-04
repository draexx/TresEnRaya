# This is a sample Python script.
import os

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
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
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
    def __init__(self, tipo, nombre=""):
        self.tipo = tipo
        self.nombre = nombre if nombre else f"Jugador {tipo}"

    def __str__(self):
        return self.nombre


class Juego:
    def __init__(self, nombre_jugador1="", nombre_jugador2=""):
        self.jugador1 = Ficha("X", nombre_jugador1)
        self.jugador2 = Ficha("O", nombre_jugador2)
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


def solicitar_nombres_jugadores():
    nombre_j1 = input("Ingrese el nombre para el Jugador X (o presione Enter para 'Jugador X'): ")
    nombre_j2 = input("Ingrese el nombre para el Jugador O (o presione Enter para 'Jugador O'): ")
    return nombre_j1, nombre_j2

def solicitar_numero_partidas():
    while True:
        try:
            num_partidas = int(input("¿Cuántas partidas desean jugar?: "))
            if num_partidas > 0:
                return num_partidas
            else:
                print("Por favor, ingrese un número mayor que cero.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def jugar_una_partida(juego):
    #juego = Juego() # Se pasa el juego como argumento
    juego.tablero = Tablero() # Reiniciar tablero para cada partida
    juego.imprimir_jugada_valida()
    jugador_actual = juego.jugador1
    movimientos_realizados = 0
    max_movimientos = 9

    while movimientos_realizados < max_movimientos:
        juego.imprimiendo_tablero() # This will now clear the screen and print the board
        print(f"Turno del {jugador_actual}")
        posicion = input("¿Cuál es tu movimiento? (ej. SI, CC, ID): ").upper()

        # La validación de la posición y el registro del movimiento ahora están encapsulados en modificar_tablero
        juego.modificar_tablero(posicion, jugador_actual.tipo)
        movimientos_realizados += 1

        if juego.ganador_juego(jugador_actual):
            juego.imprimiendo_tablero() # Ensure the final board state is shown
            print(f"¡Felicidades {jugador_actual}! Has ganado la partida.")
            return jugador_actual # Devuelve el ganador
        if movimientos_realizados == max_movimientos:
            juego.imprimiendo_tablero() # Ensure the final board state is shown
            print("La partida ha terminado en empate.")
            return None # Indica empate

        jugador_actual = juego.cambiar_turno(jugador_actual)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("¡Bienvenido a Tres en Raya!")
    nombre_j1, nombre_j2 = solicitar_nombres_jugadores()
    num_partidas_total = solicitar_numero_partidas()

    juego_actual = Juego(nombre_j1, nombre_j2)
    puntuacion = {juego_actual.jugador1.nombre: 0, juego_actual.jugador2.nombre: 0, "empates": 0}

    for i in range(num_partidas_total):
        print(f"\n--- Partida {i + 1} de {num_partidas_total} ---")
        ganador_partida = jugar_una_partida(juego_actual)
        if ganador_partida:
            puntuacion[ganador_partida.nombre] += 1
        else:
            puntuacion["empates"] += 1

        print("\nPuntuación actual:")
        for nombre, puntos in puntuacion.items():
            if nombre != "empates":
                print(f"{nombre}: {puntos} victorias")
        print(f"Empates: {puntuacion['empates']}")

    print("\n--- ¡Juego Terminado! ---")
    print("Puntuación final:")
    # Determinar el ganador general o si fue empate general
    punt_j1 = puntuacion[juego_actual.jugador1.nombre]
    punt_j2 = puntuacion[juego_actual.jugador2.nombre]

    if punt_j1 > punt_j2:
        print(f"¡{juego_actual.jugador1.nombre} es el ganador general con {punt_j1} victorias!")
    elif punt_j2 > punt_j1:
        print(f"¡{juego_actual.jugador2.nombre} es el ganador general con {punt_j2} victorias!")
    else:
        print(f"¡El juego ha terminado en un empate general con {punt_j1} victorias cada uno!")

    for nombre, puntos in puntuacion.items():
        if nombre != "empates":
            print(f"{nombre}: {puntos} victorias")
    print(f"Empates: {puntuacion['empates']}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
