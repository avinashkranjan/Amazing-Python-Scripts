import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.configure(text="Your BMI is: " + str(bmi))

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_label.configure(text="Your BMI is: ")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_entry = tk.Entry(root)

height_label = tk.Label(root, text="Height (m):")
height_entry = tk.Entry(root)

bmi_label = tk.Label(root, text="Your BMI is: ")

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)

weight_label.grid(row=0, column=0)
weight_entry.grid(row=0, column=1)
height_label.grid(row=1, column=0)
height_entry.grid(row=1, column=1)
bmi_label.grid(row=2, column=0)
calculate_button.grid(row=3, column=0)
clear_button.grid(row=3, column=1)

root.mainloop()
