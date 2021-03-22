from tkinter import *
from playsound import playsound
import datetime
import time
from threading import *


root = Tk() 
  
# Set geometry 
root.geometry("600x400") 
  
# Use Threading 
def Threading(): 
    t1=Thread(target=alarm) 
    t1.start() 
  
def alarm(): 
    # Infintite Loop 
    while True: 
        # Set Alarm  
        set_time = f"{hour.get()}:{minute.get()}:{second.get()}"
  
        # Wait for one seconds 
        time.sleep(1) 
  
        # Get current time 
        current_time = datetime.datetime.now().strftime("%H:%M:%S") 
        print(current_time,set_time) 
  
        # Check whether set alarm is equal to current time or not 
        if current_time == set_time: 
            print("Time to Wake up") 
            # Playing sound 
            playsound('alarm.wav') 
  
    
  
# Add Labels, Frame, Button, Optionmenus 
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10) 
Label(root, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
Label(root,text = "Hour  Min   Sec",font=60).place(x = 110,y=40)
Label(root,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=80)
  
frame = Frame(root) 
frame.pack() 
  
hour = StringVar()
minute = StringVar()
second = StringVar()
Entry(root,textvariable = hour,bg = "white",width = 15).place(x=110,y=80)
Entry(root,textvariable = minute,bg = "white",width = 15).place(x=150,y=80)
Entry(root,textvariable = second,bg = "white",width = 15).place(x=200,y=80)

  
Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=120) 
  
# Execution
root.mainloop()
