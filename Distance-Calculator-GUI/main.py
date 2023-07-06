from tkinter import *
from geopy.geocoders import Nominatim
from geopy import distance

# user defined funtion


def get_dis():
    try:

        geolocator = Nominatim(user_agent="geoapiExercises")

        place1 = geolocator.geocode(str(e1.get()))
        place2 = geolocator.geocode(str(e2.get()))

        Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
        Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

        location1 = (Loc1_lat, Loc1_lon)
        location2 = (Loc2_lat, Loc2_lon)

        res = (str(distance.distance(location1, location2).km) + " Km")

        result.set(res)
    except:
        result.set("someting went wrong")


# object of tkinter
# with background set to light grey
master = Tk()
master.configure(bg='light grey')
master.title("Distance Calculating App")

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter first place : ", bg="light grey").grid(row=1,
                                                                 sticky=W)
Label(master, text="Enter secound place : ", bg="light grey").grid(row=2,
                                                                   sticky=W)

Label(master, text="Result :", bg="light grey").grid(row=3, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result, bg="light grey").grid(row=3,
                                                                  column=1,
                                                                  sticky=W)

e1 = Entry(master, width=50)
e1.grid(row=1, column=1)
e2 = Entry(master, width=50)
e2.grid(row=2, column=1)

# creating a button using the widget
b = Button(master, text="Check", command=get_dis, bg="white")
b.grid(
    row=1,
    column=2,
    columnspan=2,
    rowspan=2,
    padx=5,
    pady=5,
)

mainloop()
