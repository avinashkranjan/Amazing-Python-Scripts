# Importing required modules
import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Creating function to get temperature


def get_temp():
    # Taking City You Want to Check Temperature
    city = city_entry.get()
    # Storing City You Want to Check Temperature
    search = "weather in" + city
    # Searching it on google
    url = f"https://www.google.com/search?&q={search}"
    # Sending and Receiving Requests
    r = requests.get(url)
    # Scrape the temperature from the search results
    s = BeautifulSoup(r.text, "html.parser")
    # Storing details
    update = s.find("div", class_="BNeawe").text
    # Display the temperature
    temperature_label.config(text="Temperature in " + city + " is: " + update)


# Creating the main window
root = tk.Tk()
root.geometry('200x200')

# Creating label for city
city_label = tk.Label(root, text="City: ")

# Creating entry widget for city
city_entry = tk.Entry(root)

# Creating button to get temperature
get_temperature_button = tk.Button(
    root, text="Get Temperature", command=get_temp)

# Displaying the temperature
temperature_label = tk.Label(root)

# Positioning the widgets
city_label.pack()
city_entry.pack()
get_temperature_button.pack()
temperature_label.pack()

# Starting main loop
root.mainloop()
