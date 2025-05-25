import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors 🎮")
        self.root.geometry("400x300")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ttk.Label(self.root, text="Rock Paper Scissors", font=("Helvetica", 16))
        title.pack(pady=10)
        
        # Buttons
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=10)
        
        ttk.Button(buttons_frame, text="🪨 Rock", command=lambda: self.play("rock")).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="📄 Paper", command=lambda: self.play("paper")).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="✂️ Scissors", command=lambda: self.play("scissors")).pack(side=tk.LEFT, padx=5)
        
        # Result Label
        self.result_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)
        
        # Score Label
        self.score_label = ttk.Label(self.root, text="Score: You 0 - 0 Computer", font=("Helvetica", 12))
        self.score_label.pack(pady=10)
    
    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie! 🤝"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win! 🎉"
            self.user_score += 1
        else:
            result = "Computer wins! 🤖"
            self.computer_score += 1
        
        # Update UI
        self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
    