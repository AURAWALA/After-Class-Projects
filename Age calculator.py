import tkinter as tk
from tkinter import messagebox
from datetime import date



def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        today = date.today()
        dob = date(year, month, day)


        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for day, month, and year.")



root = tk.Tk()
root.title("Age Calculator")


tk.Label(root, text="Enter Day:").grid(row=0, column=0, padx=10, pady=5)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Month:").grid(row=1, column=0, padx=10, pady=5)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Year:").grid(row=2, column=0, padx=10, pady=5)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1, padx=10, pady=5)


calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)


root.mainloop()
