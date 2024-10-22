##############################
#Creado por Jorge Barreto
#ID: 000484006
#Universidad Pontificia Bolivariana
##############################


import tkinter as tk
import random

class TrikiGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Triki Triki")
        self.player_turn = "X"
        self.game_over = False
        self.buttons = []
        self.score_x = 0
        self.score_o = 0
        # Inicializamos el modo por defecto
        self.mode = "two_players"  # Añadido: inicialización del modo
        self.create_buttons()
        self.create_scoreboard()
        self.create_mode_buttons()
        self.time_label = tk.Label(master, text="Time: 0", font=("Arial", 14))
        self.time_label.grid(row=4, column=0, columnspan=3)
        self.time_elapsed = 0
        self.update_time()

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def create_scoreboard(self):
        self.score_label = tk.Label(self.master, text=f"X: {self.score_x} O: {self.score_o}", font=("Arial", 14))
        self.score_label.grid(row=3, column=0, columnspan=3)

    def create_mode_buttons(self):
        self.mode_frame = tk.Frame(self.master)
        self.mode_frame.grid(row=5, column=0, columnspan=3)
        self.two_player_button = tk.Button(self.mode_frame, text="2 Players", command=self.set_two_players)
        self.two_player_button.pack(side=tk.LEFT)
        self.computer_button = tk.Button(self.mode_frame, text="Against Computer", command=self.set_computer)
        self.computer_button.pack(side=tk.LEFT)

    def set_two_players(self):
        self.mode = "two_players"
        self.reset_game()

    def set_computer(self):
        self.mode = "computadora"
        self.reset_game()

    def click(self, row, column):
        if self.game_over or self.buttons[row][column]['text'] != "":
            return

        # Realiza el movimiento del jugador X
        if self.player_turn == "X":
            self.buttons[row][column]['text'] = "X"
            if self.check_win():
                self.game_over = True
                self.update_score()
                self.master.title("Triki Triki - X Ganó!")
                return
            
            # Cambia el turno solo si no hay ganador
            self.player_turn = "O"
            
            # Si estamos en modo computadora, realiza el movimiento de la computadora
            if self.mode == "computadora" and not self.game_over:
                self.master.after(500, self.computer_move)  # Añade un pequeño retraso para mejor visualización

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

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def update_score(self):
        if self.player_turn == "X":
            self.score_x += 1
        else:
            self.score_o += 1
        self.score_label.config(text=f"X: {self.score_x} O: {self.score_o}")

    def reset_game(self):
        self.player_turn = "X"
        self.game_over = False
        self.master.title("Triki Triki")
        for row in self.buttons:
            for button in row:
                button['text'] = ""

    def computer_move(self):
        if self.game_over:
            return
            
        empty_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if empty_buttons:
            row, column = random.choice(empty_buttons)
            self.buttons[row][column]['text'] = "O"
            
            if self.check_win():
                self.game_over = True
                self.update_score()
                self.master.title("Triki Triki - O Ganó!")
            elif self.check_draw():
                self.game_over = True
                self.master.title("Triki Triki - Empate!")
            else:
                self.player_turn = "X"

    def update_time(self):
        if not self.game_over:
            self.time_elapsed += 1
            self.time_label.config(text=f"Time: {self.time_elapsed}")
            self.master.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    game = TrikiGame(root)
    root.mainloop()