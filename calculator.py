import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("Simple Calculator")


entry = tk.Entry(window, width=16, font=('Arial', 18), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, column) in buttons:
    if text == 'C':
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=clear_entry)
    elif text == '=':
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=calculate)
    else:
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda value=text: on_button_click(value))

    button.grid(row=row, column=column)

window.mainloop()
