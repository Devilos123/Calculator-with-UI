import tkinter as tk
from tkinter import messagebox
import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def exponentiate(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    return math.sqrt(x)


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Exponentiate":
            result = exponentiate(num1, num2)
        elif operation == "Square Root":
            result = square_root(num1)
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# Create the main window
root = tk.Tk()
root.title("Shresh Calculator")

# Maximize the window
root.state('zoomed')

# Configure grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Create and place the input fields and labels
tk.Label(root, text="First Number:", font=("Arial", 34)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry1 = tk.Entry(root, font=("Arial", 14), width=15)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Second Number:", font=("Arial", 34)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry2 = tk.Entry(root, font=("Arial", 14), width=15)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create a dropdown for operation selection
operation_var = tk.StringVar(root)
operation_var.set("Add")  # Default value
operations = ["Add", "Subtract", "Multiply", "Divide", "Exponentiate", "Square Root"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(font=("Arial", 34))
operation_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 34), width=15)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 34))
result_label.grid(row=4, column=0, columnspan=7, padx=50, pady=10)

# Start the GUI event loop
root.mainloop()



