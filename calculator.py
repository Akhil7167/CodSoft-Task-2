import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Please select an operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers.")

# Set up window
root = tk.Tk()
root.title(" Calculator")

# Inputs
tk.Label(root, text="First Number:").grid(row=0, column=0, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Operation dropdown
tk.Label(root, text="Operation:").grid(row=2, column=0, pady=5)
operation_var = tk.StringVar(value='+')
operations = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operations.grid(row=2, column=2)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
