import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter positive values.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")

tk.Label(root, text="Weight (kg)").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()