from tkinter import *
import datetime
import time
import pygame
import threading
import sys
from threading import Thread

pygame.mixer.init(42050, -16, 2, 2048)
alarm_sound = pygame.mixer.Sound("alarm.wav")

def Threading():
    t1=Thread(target=actual_time) 
    t1.start()
 
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            pygame.mixer.Sound.play(alarm_sound, loops = -1)
            time.sleep(30)
            break
            
        
def actual_time():
    set_alarm_timer = f"{hour.get()}:{mins.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    

clock = Tk()
def on_closing():
    pygame.mixer.Sound.stop(alarm_sound)
    clock.destroy()
    sys.exit()

clock.protocol("WM_DELETE_WINDOW", on_closing) 
clock.geometry("400x200")
Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
 
# The Variables we require to set the alarm(initialization):
hour = StringVar()
mins = StringVar()
sec = StringVar()
 
#Time required to set the alarm clock:
Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=110,y=30)
Entry(clock,textvariable = mins,bg = "white",width = 15).place(x=150,y=30)
Entry(clock,textvariable = sec,bg = "white",width = 15).place(x=200,y=30)

 
#To take the time input by user:
Button(clock,text = "Set Alarm",fg="red",width = 10,command = Threading).place(x =110,y=70)
 
clock.mainloop()
#Execution of the window.
