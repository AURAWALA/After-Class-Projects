import tkinter as tk
from tkinter import messagebox



def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())


        simple_interest = (principal * rate * time) / 100


        compound_interest = principal * ((1 + rate / 100) ** time) - principal


        result_label.config(
            text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")



root = tk.Tk()
root.title("Interest Calculator")


tk.Label(root, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Time (years):").grid(row=1, column=0, padx=10, pady=5)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Interest Rate (%):").grid(row=2, column=0, padx=10, pady=5)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=5)


calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
