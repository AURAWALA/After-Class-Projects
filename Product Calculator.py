import tkinter as tk


def calculate_product():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    result_label.config(text="Product: " + str(result))


window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x250")


label1 = tk.Label(window, text="Enter First Number:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Enter Second Number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Calculate Product", command=calculate_product)
button.pack(pady=10)


result_label = tk.Label(window, text="Product: ")
result_label.pack()


window.mainloop()
