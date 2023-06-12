# This is a sample Python script.

# Press Mays+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Tablero:
    def __init__(self):
        self.tablero = {"SI": " ", "CI": " ", "II": " ",
                        "SC": " ", "CC": " ", "IC": " ",
                        "SD": " ", "CD": " ", "ID": " "}

    def imprimir_tablero(self):
        print(self.tablero["SI"] + "|" + self.tablero["SC"] + "|" + self.tablero["SD"])
        print("-+" * 2 + "-")
        print(self.tablero["CI"] + "|" + self.tablero["CC"] + "|" + self.tablero["CD"])
        print("-+" * 2 + "-")
        print(self.tablero["II"] + "|" + self.tablero["IC"] + "|" + self.tablero["ID"])

    def movimiento_valido(self, posicion):
        if self.tablero[posicion] == " ":
            return True
        return False

    def registro_movimiento(self, posicion, tipo):
        if self.movimiento_valido(posicion):
            self.tablero[posicion] = tipo
            return self.tablero
        return None

    def ganador(self, jugador):
        jugador_tipo = jugador.tipo
        jugadas = [
            # horizontal
            ["SI", "SC", "SD"],
            ["CI", "CC", "CD"],
            ["II", "IC", "ID"],
            # vertical
            ["SI", "CI", "II"],
            ["SC", "CC", "IC"],
            ["SD", "CD", "ID"],
            # diagonal
            ["SI", "CC", "ID"],
            ["II", "CC", "SD"]
        ]

        for a, b, c in jugadas:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] == jugador_tipo:
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
        if self.tablero.registro_movimiento(posicion, tipo) is not None:
            return self.tablero.registro_movimiento(posicion, tipo)
        else:
            posicion = input("Posicion no valida. Intente de nuevo")
            return self.tablero.registro_movimiento(posicion, tipo)


def jugar():
    juego = Juego()
    juego.imprimir_jugada_valida()
    jugador = juego.jugador1
    num = 9
    while num > 0:
        num -= 1
        juego.imprimiendo_tablero()
        posicion = input("{} Turno, cual es el movimiento? ".format(jugador))
        juego.modificar_tablero(posicion, jugador.tipo)
        if juego.ganador_juego(jugador):
            print("{} es ganador".format(jugador))
            break
        else:
            jugador = juego.cambiar_turno(jugador)

    if num == 0:
        print("Juego Terminado")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jugar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
