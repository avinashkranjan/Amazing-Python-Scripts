import time
import pyautogui
import tkinter as tk
from tkinter import ttk


def take_screenshot(delay):
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)  # To name the file
    time.sleep(delay)  # Time Wait Before Taking Screenshot
    img = pyautogui.screenshot(name)
    img.show()  # To Show the Screenshot After Being Taken


def on_take_screenshot():
    delay = float(delay_entry.get())
    take_screenshot(delay)


# Create the tkinter GUI
root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("300x150")

# Label and Entry for specifying the time delay
delay_label = ttk.Label(root, text="Delay (in seconds):")
delay_label.pack(pady=10)
delay_entry = ttk.Entry(root)
delay_entry.pack(pady=5)
delay_entry.insert(0, "5.0")  # Default value

# Button to trigger the screenshot capture
screenshot_button = ttk.Button(
    root, text="Take Screenshot", command=on_take_screenshot)
screenshot_button.pack(pady=20)

root.mainloop()
