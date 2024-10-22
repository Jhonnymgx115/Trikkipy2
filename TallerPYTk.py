##############################
#Creado por Jorge Barreto
#ID: 000484006
#Universidad Pontificia Bolivariana
##############################


import tkinter as tk
import random

# Clase principal del juego Triki
class TrikiGame:
    def __init__(self, master):
        # Inicialización de la ventana principal y variables del juego
        self.master = master
        self.master.title("Triki Triki")
        self.player_turn = "X"  # Comienza el jugador X
        self.game_over = False  # Indica si el juego ha terminado
        self.buttons = []  # Matriz que almacenará los botones del tablero
        self.score_x = 0  # Puntuación para el jugador X
        self.score_o = 0  # Puntuación para el jugador O
        self.create_buttons()  # Crea los botones del tablero
        self.create_scoreboard()  # Crea el marcador
        self.create_mode_buttons()  # Crea los botones para elegir el modo de juego
        self.time_label = tk.Label(master, text="Time: 0", font=("Arial", 14))  # Etiqueta para mostrar el tiempo
        self.time_label.grid(row=4, column=0, columnspan=3)  # Posiciona la etiqueta del temporizador
        self.time_elapsed = 0  # Tiempo transcurrido en el juego
        self.update_time()  # Inicia el temporizador

    # Método para crear los botones del tablero 3x3
    def create_buttons(self):
        for i in range(3):  # Filas
            row = []
            for j in range(3):  # Columnas
                # Crea un botón vacío y lo agrega al grid
                button = tk.Button(self.master, command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)  # Añade la fila de botones a la matriz

    # Crea el marcador que muestra las puntuaciones
    def create_scoreboard(self):
        self.score_label = tk.Label(self.master, text=f"X: {self.score_x} O: {self.score_o}", font=("Arial", 14))
        self.score_label.grid(row=3, column=0, columnspan=3)  # Posiciona el marcador debajo del tablero

    # Crea los botones para elegir entre jugar contra otro jugador o contra la computadora
    def create_mode_buttons(self):
        self.mode_frame = tk.Frame(self.master)  # Frame para los botones de modo
        self.mode_frame.grid(row=5, column=0, columnspan=3)  # Posiciona el frame debajo del marcador
        self.two_player_button = tk.Button(self.mode_frame, text="2 Players", command=self.set_two_players)
        self.two_player_button.pack(side=tk.LEFT)  # Botón para el modo de 2 jugadores
        self.computer_button = tk.Button(self.mode_frame, text="Against Computer", command=self.set_computer)
        self.computer_button.pack(side=tk.LEFT)  # Botón para el modo contra la computadora

    # Configura el juego para el modo de 2 jugadores
    def set_two_players(self):
        self.mode = "two_players"  # Establece el modo actual
        self.reset_game()  # Reinicia el juego

    # Configura el juego para el modo contra la computadora
    def set_computer(self):
        self.mode = "computadora"  # Establece el modo actual
        self.reset_game()  # Reinicia el juego

    # Método que maneja la acción al hacer clic en una celda
    def click(self, row, column):
        if self.game_over:  # Si el juego ha terminado, no hacer nada
            return
        if self.buttons[row][column]['text'] == "":  # Solo permite mover si la celda está vacía
            self.buttons[row][column]['text'] = self.player_turn  # Coloca la marca del jugador actual
            if self.check_win():  # Revisa si el jugador ha ganado
                self.game_over = True
                self.update_score()  # Actualiza la puntuación
                self.master.title(f"Triki Triki - {self.player_turn} Gano!")  # Muestra quién ganó en el título
            else:
                # Cambia de turno entre "X" y "O"
                self.player_turn = "O" if self.player_turn == "X" else "X"
                if self.mode == "computadora" and self.player_turn == "O":
                    self.computer_move()  # Si es el turno de la computadora, hace su jugada

    # Método para verificar si algún jugador ha ganado
    def check_win(self):
        # Revisa filas
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        # Revisa columnas
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        # Revisa diagonales
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    # Método para actualizar el marcador según el jugador ganador
    def update_score(self):
        if self.player_turn == "X":
            self.score_x += 1  # Incrementa el puntaje de X
        else:
            self.score_o += 1  # Incrementa el puntaje de O
        # Actualiza la etiqueta del marcador
        self.score_label.config(text=f"X: {self.score_x} O: {self.score_o}")

    # Reinicia el juego, limpiando el tablero y restableciendo los turnos
    def reset_game(self):
        self.player_turn = "X"  # Reinicia el turno a "X"
        self.game_over = False  # El juego no ha terminado
        self.master.title("Triki Triki")  # Reinicia el título de la ventana
        # Limpia el texto de todos los botones del tablero
        for row in self.buttons:
            for button in row:
                button['text'] = ""

    # Lógica de la computadora para hacer una jugada aleatoria
    def computer_move(self):
        empty_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if empty_buttons:
            # Selecciona aleatoriamente una celda vacía
            row, column = random.choice(empty_buttons)
            self.buttons[row][column]['text'] = "O"  # La computadora juega con "O"
            if self.check_win():  # Revisa si la computadora ha ganado
                self.game_over = True
                self.update_score()  # Actualiza el marcador
                self.master.title("Triki Triki - O Gana!")  # Muestra que la computadora ganó

    # Actualiza el temporizador cada segundo
    def update_time(self):
        if not self.game_over:  # Si el juego no ha terminado, continúa contando
            self.time_elapsed += 1  # Incrementa el tiempo
            self.time_label.config(text=f"Time: {self.time_elapsed}")  # Actualiza la etiqueta del temporizador
            # Programa la siguiente actualización del tiempo en 1 segundo
            self.master.after(1000, self.update_time)

# Crea la ventana principal y ejecuta el juego
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de tkinter
    game = TrikiGame(root)  # Instancia la clase TrikiGame
    root.mainloop()  # Inicia el loop de la interfaz gráfica