import tkinter as tk
from tkinter import messagebox
import math


# Button click function
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))


# Clear the entry
def button_clear():
    entry.delete(0, tk.END)


# Perform the calculation
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")


# Add scientific functions
def scientific_function(func):
    try:
        current = entry.get()
        result = str(func(float(current)))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")


# Initialize main window
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#2b2b2b")
root.geometry("400x500")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, width=28, borderwidth=3, font=('Arial', 18), justify='right', bg="#eeeeee", fg="#000000")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

# Button layout and style
button_font = ('Arial', 12, 'bold')
button_bg = "#444444"
button_fg = "#ffffff"
button_hover_bg = "#666666"


def on_enter(event, btn):
    btn['background'] = button_hover_bg


def on_leave(event, btn):
    btn['background'] = button_bg


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3), ('=', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('pi', 5, 3), ('e', 5, 4),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=6, height=2, font=button_font, bg="#009688", fg="#ffffff",
                        command=button_equal)
    elif text == "C":
        btn = tk.Button(root, text=text, width=6, height=2, font=button_font, bg="#e53935", fg="#ffffff",
                        command=button_clear)
    elif text in ("sqrt", "log", "sin", "cos", "tan"):
        func_map = {
            "sqrt": math.sqrt,
            "log": math.log,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan
        }
        btn = tk.Button(root, text=text, width=6, height=2, font=button_font, bg=button_bg, fg=button_fg,
                        command=lambda f=func_map[text]: scientific_function(f))
    elif text in ("pi", "e"):
        value_map = {
            "pi": math.pi,
            "e": math.e
        }
        btn = tk.Button(root, text=text, width=6, height=2, font=button_font, bg=button_bg, fg=button_fg,
                        command=lambda v=value_map[text]: button_click(v))
    elif text == "^":
        btn = tk.Button(root, text=text, width=6, height=2, font=button_font, bg=button_bg, fg=button_fg,
                        command=lambda: button_click("**"))
    else:
        btn = tk.Button(root, text=text, width=6, height=2, font=button_font, bg=button_bg, fg=button_fg,
                        command=lambda t=text: button_click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

# Run the application
root.mainloop()
