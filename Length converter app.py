import tkinter as tk
from tkinter import messagebox


def convert_to_cm():
    try:
        inches = float(inches_entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


root = tk.Tk()
root.title("Inches to Centimeters Converter")


tk.Label(root, text="Enter length in inches:").grid(row=0, column=0, padx=10, pady=10)
inches_entry = tk.Entry(root)
inches_entry.grid(row=0, column=1, padx=10, pady=10)


convert_button = tk.Button(root, text="Convert to cm", command=convert_to_cm)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
