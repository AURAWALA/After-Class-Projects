import tkinter as tk
from tkinter import messagebox
import random



def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = f"Draw! Both chose {choice}"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
            (choice == "Paper" and computer_choice == "Rock") or \
            (choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! Computer chose {computer_choice}"
    else:
        result = f"You Lose! Computer chose {computer_choice}"

    result_label.config(text=result)



root = tk.Tk()
root.title("Rock Paper Scissors Game")


tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)


result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)


root.mainloop()