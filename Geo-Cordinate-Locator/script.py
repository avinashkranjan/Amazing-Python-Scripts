from tkinter import *
from geopy.geocoders import ArcGIS
import clipboard


def f():
    s = e1.get()
    nom = ArcGIS()
    n = nom.geocode(s)
    x = n.latitude
    y = n.longitude
    t.delete(first=0, last=len(t1.get()))
    u.delete(first=0, last=len(u1.get()))
    t.insert(END, str(x))
    u.insert(END, str(y))


def g():
    x = t1.get()
    y = u1.get()
    s = ""
    s = s + "Latitude=> " + x
    s = s + " "
    s = s + "Longitude=> " + y
    # print(s)
    clipboard.copy(s)


window = Tk()
window.title("Geocordinate Detector")
window.resizable(0, 0)

l1 = Label(window, text="Enter your Address")
l1.grid(row=0, column=0)

e1 = StringVar()
e = Entry(window, textvariable=e1, width=50)
e.grid(row=0, column=1)

b1 = Button(window, text="Locate Me!", width=40, command=f)
b1.grid(row=1, column=0, columnspan=2)

l2 = Label(window, text="Latitude")
l2.grid(row=2, column=0)

l3 = Label(window, text="Longitude")
l3.grid(row=3, column=0)

t1 = StringVar()
t = Entry(window, textvariable=t1, width=50)
t.grid(row=2, column=1)

u1 = StringVar()
u = Entry(window, textvariable=u1, width=50)
u.grid(row=3, column=1)

b2 = Button(window, text="Copy", width=40, command=g)
b2.grid(row=4, column=0, columnspan=2)

window.mainloop()
