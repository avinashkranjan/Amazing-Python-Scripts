import tkinter as tk


def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == 0:  # Celsius to Fahrenheit
            result = temperature * 9/5 + 32
            output_label.configure(text=f"{temperature}°C = {result}°F")
        elif var.get() == 1:  # Fahrenheit to Celsius
            result = (temperature - 32) * 5/9
            output_label.configure(text=f"{temperature}°F = {result}°C")
    except ValueError:
        output_label.configure(text="Invalid input")


# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create input label and entry widget
input_label = tk.Label(window, text="Enter temperature:")
input_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create radio buttons for temperature conversion options
var = tk.IntVar()
celsius_to_fahrenheit = tk.Radiobutton(
    window, text="Celsius to Fahrenheit", variable=var, value=0)
celsius_to_fahrenheit.pack()
fahrenheit_to_celsius = tk.Radiobutton(
    window, text="Fahrenheit to Celsius", variable=var, value=1)
fahrenheit_to_celsius.pack()

# Create convert button
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Create output label for displaying result
output_label = tk.Label(window)
output_label.pack()

# Run the main event loop
window.mainloop()
