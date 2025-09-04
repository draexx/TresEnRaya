import tkinter as tk
from tkinter import font

# --- Game Logic Classes (from main_console.py) ---

class Tablero:
    def __init__(self):
        self.tablero_interno = [[" " for _ in range(3)] for _ in range(3)]

    def movimiento_valido(self, fila, columna):
        return self.tablero_interno[fila][columna] == " "

    def registro_movimiento(self, fila, columna, tipo):
        if self.movimiento_valido(fila, columna):
            self.tablero_interno[fila][columna] = tipo
            return True
        return False

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

    def is_full(self):
        return all(self.tablero_interno[row][col] != " " for row in range(3) for col in range(3))


class Ficha:
    def __init__(self, tipo, nombre=""):
        self.tipo = tipo
        self.nombre = nombre if nombre else f"Jugador {tipo}"

    def __str__(self):
        return self.nombre

class Juego:
    def __init__(self, nombre_jugador1="Jugador X", nombre_jugador2="Jugador O"):
        self.jugador1 = Ficha("X", nombre_jugador1)
        self.jugador2 = Ficha("O", nombre_jugador2)
        self.tablero = Tablero()

    def cambiar_turno(self, ficha):
        return self.jugador2 if ficha is self.jugador1 else self.jugador1

    def ganador_juego(self, jugador):
        return self.tablero.ganador(jugador)

# --- GUI Class ---

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tres en Raya")
        self.window.resizable(False, False)

        self.juego = Juego()
        self.jugador_actual = self.juego.jugador1
        self.game_over = False

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=font.Font(size=24, weight="bold"),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        self.status_label = tk.Label(
            self.window,
            text=f"Turno de {self.jugador_actual.nombre}",
            font=font.Font(size=16)
        )
        self.status_label.pack(pady=10)

        self.play_again_button = tk.Button(
            self.window,
            text="Jugar de Nuevo",
            font=font.Font(size=14),
            command=self.reset_game
        )
        self.play_again_button.pack(pady=10)

    def on_button_click(self, row, col):
        if self.game_over or not self.juego.tablero.movimiento_valido(row, col):
            return

        # Update game logic and GUI
        self.juego.tablero.registro_movimiento(row, col, self.jugador_actual.tipo)
        self.buttons[row][col].config(text=self.jugador_actual.tipo, state=tk.DISABLED)

        # Check for winner
        if self.juego.ganador_juego(self.jugador_actual):
            self.status_label.config(text=f"¡{self.jugador_actual.nombre} ha ganado!")
            self.end_game()
            return

        # Check for draw
        if self.juego.tablero.is_full():
            self.status_label.config(text="¡Es un empate!")
            self.end_game()
            return

        # Switch player
        self.jugador_actual = self.juego.cambiar_turno(self.jugador_actual)
        self.status_label.config(text=f"Turno de {self.jugador_actual.nombre}")

    def end_game(self):
        self.game_over = True
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def reset_game(self):
        self.game_over = False
        self.juego.tablero = Tablero()
        self.jugador_actual = self.juego.jugador1
        self.status_label.config(text=f"Turno de {self.jugador_actual.nombre}")

        for row in self.buttons:
            for button in row:
                button.config(text="", state=tk.NORMAL)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game_gui = TicTacToeGUI()
    game_gui.run()
