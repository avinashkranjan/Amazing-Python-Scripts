import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pygame

#Initializing the wav alarm file we want it to play when the alarm goes 
pygame.mixer.init(42050, -16, 2, 2048)
alarm_sound = pygame.mixer.Sound("./Alarm-Clock/alarm.wav")
#Setting the initial global values
start_printed = False
stop_printed = True
done = False
finished = False
stop_clicked = False

class AlarmApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #Title of the window set to 'Alarm Clock'
        self.title("Alarm Clock")
        #Set up all of the drop-down lists
        self.hr = tk.IntVar(self)
        self.min = tk.IntVar(self)
        self.ampm = tk.StringVar(self)
        #Set the initial values of each drop-down list
        self.hr.set('12')
        self.min.set("00")
        self.ampm.set("AM")
        #Create the list of values for drop down list 
        hours = []
        minutes = []
        ampmlist = ["AM","PM"]
        #Hours go from 1 to 12
        for x in range(1,13):
            hours.append(x)
        #Minutes go from 0 to 59
        for y in range(0,60):
            minutes.append("%02d" % (y,))
            #Placing all of the list into the respective drop-down list
        self.popmenuhours = tk.OptionMenu(self,self.hr, *hours)
        self.popmenuminutes = tk.OptionMenu(self,self.min, *minutes)
        self.popmenuAMPM = tk.OptionMenu(self, self.ampm, *ampmlist)
        #Placing our drop-down lists on the page as well as one label
        self.popmenuhours.pack(side = "left")
        self.thing = tk.Label(text = ":").pack(side = "left")
        self.popmenuminutes.pack(side = "left")
        self.popmenuAMPM.pack(side = "left")
        #Setting up all the buttons on the right hand side of the window.
        #Command refers to which function it will run once it's clicked
        #State refers to whether it is clickable or not at the current state.
        self.alarmbutton = tk.Button(self, text="Set Alarm", command=self.start_clock)
        self.cancelbutton = tk.Button(self, text="Cancel Alarm", command=self.stop_clock, state = "disabled")
        self.stopalarmbutton = tk.Button(self, text = "Stop Alarm", command=self.stop_audio, state = "disabled")
        #Packing all the buttons into the page
        self.alarmbutton.pack()
        self.cancelbutton.pack()
        self.stopalarmbutton.pack()

    def start_clock(self):

        global done, start_printed, stop_printed, stop_clicked
        #Done refers to whether either the time has been reached or if the user has cancelled. I.e: Loop is done.
        if done == False:
            #Cancel button is now active so user can decide at any point to cancel the alarm
            self.cancelbutton.config(state = "active")
            #Alarm button is now disabled since an alarm has currently already been set
            self.alarmbutton.config(state = "disabled")
            #On the first run of the loop, let the user know that an alarm has been set for their desired time
            if start_printed == False:
                #Print this notification for the user in the terminal
                print("Alarm set for {}:{}{}".format(self.hr.get(), "%02d" % (self.min.get()),self.ampm.get()))
                start_printed = True
                stop_printed = False
           
            if self.ampm.get() == "AM":
                if self.hr.get() in range(1,12):
                    hour_value = self.hr.get()
                else:
                    hour_value = self.hr.get() - 12
            if self.ampm.get() == "PM":
                if self.hr.get() in range(1,12):
                    hour_value = self.hr.get() +12
                else:
                    hour_value = self.hr.get()
            #Now we call the Alarm function with the information that the user has entered to check whether we have reached the alarm time
            self.Alarm("%02d" % (hour_value,), "%02d" % (self.min.get()))
        #If user has clicked the cancel alarm button, we reset everything
        if stop_clicked == True:
            done = False
            start_printed = False
            stop_clicked = False

    def stop_clock(self):
        global done, stop_clicked
        #Let the user know that the alarm has been cancelled by printing it in the terminal
        print("Alarm set for {}:{}{} has been cancelled".format(self.hr.get(), "%02d" % (self.min.get()),self.ampm.get()))
        #Cancel button has now been clicked
        stop_clicked = True
        #Now done with the current alarm/loop
        done = True
        #Buttons reset to what they were originally
        self.cancelbutton.config(state = "disabled")
        self.alarmbutton.config(state = "active")

    def stop_audio(self):
        #Use PyGame to stop the audio since button has been clicked
        pygame.mixer.Sound.stop(alarm_sound)
        #Stop alarm button disabled and alarm button active, essentially reseting everything
        self.stopalarmbutton.config(state = "disabled")
        self.alarmbutton.config(state = "active")



    def Alarm(self,myhour,myminute):
        global done, start_printed, finished
        #If we are still not done, we follow this statement
        if done == False:
            #We convert the information into strings (To match DateTime)
            myhour,myminute = str(myhour),str(myminute)
            #Next, we extract the data of the current time from DateTime and take the information we want (hour and minute)
            a = str(datetime.now())
            b = a.split(" ")[1].split(":")
            hour = b[0]
            minute = b[1]
            #Now, if the alarm time matches the current time, we follow his statement. Alarm is going to go off!
            if hour == myhour and minute == myminute:
                #Using pygame to play audio, loops = -1 refers to an infinite loop
                pygame.mixer.Sound.play(alarm_sound, loops = -1)
                print("Alarm is ringing!")
                #We are now done
                done = True
                #Also finished
                finished = True
                #Now we change back the state of the cancel button to disabled, and the state of the alarm stop to active
                #This is so the user can stop the alarm, since it will infinitely loop
                self.cancelbutton.config(state = "disabled")
                self.stopalarmbutton.config(state = "active")

            else:
                #If it is still not the set time, recursively loop back to the start_clock function
                self.after(1000, self.start_clock)
            done = False
        #If it is finished, which we are when the alarm goes off, we reset everything
        if finished == True:
            start_printed = False
            finished = False

app = AlarmApp()
app.mainloop()
