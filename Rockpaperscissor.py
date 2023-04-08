import tkinter as tk
from PIL import Image, ImageTk
import random

class RockPaperScissorsGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Choose your move:", font=("Arial", 18))
        self.label.pack(pady=20)

        self.rock_image = Image.open("rock.png")
        self.rock_photo = ImageTk.PhotoImage(self.rock_image)
        self.rock_button = tk.Button(self, image=self.rock_photo, command=lambda: self.play_game("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=20)

        self.paper_image = Image.open("paper.png")
        self.paper_photo = ImageTk.PhotoImage(self.paper_image)
        self.paper_button = tk.Button(self, image=self.paper_photo, command=lambda: self.play_game("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=20)

        self.scissors_image = Image.open("scissors.png")
        self.scissors_photo = ImageTk.PhotoImage(self.scissors_image)
        self.scissors_button = tk.Button(self, image=self.scissors_photo, command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=20)

        self.result_label = tk.Label(self, font=("Arial", 18))
        self.result_label.pack(pady=20)

    def play_game(self, player_move):
        moves = ["rock", "paper", "scissors"]
        computer_move = random.choice(moves)

        if player_move == computer_move:
            result = "Tie!"
        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "paper" and computer_move == "rock") or \
             (player_move == "scissors" and computer_move == "paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        self.result_label.config(text=f"Your move: {player_move}\nComputer's move: {computer_move}\n{result}")

root = tk.Tk()
app = RockPaperScissorsGame(master=root)
app.mainloop()
