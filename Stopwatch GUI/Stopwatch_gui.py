import tkinter as tk
import tkinter.font as TkFont
from datetime import datetime

def run():
    #taking the current time
    current_time = datetime.now()
    diff = current_time - start_time
    txt_var.set('%d.%02d' %(diff.seconds,diff.microseconds//10000))
    
    if work: 
        root.after(20,run) #to reschedule after 20ms,refresh display
 
#start function
def start():
    global work
    global start_time   

    if not work:
        work = True
        start_time = datetime.now()
       
        root.after(10,run)

#stop function        
def stop():
    global work
    
    work = False

#reset function   
def reset():
    
    global start_time
    start_time = datetime.now()    
    
    if not work:
        txt_var.set('0:00')
        
        
if __name__ == "__main__" :        
    work = False
    start_time = None
    
    root = tk.Tk()
    root.geometry("500x174") #width x height
    root.title("My StopWatch")
    
    txt_var = tk.StringVar()
    txt_var.set('0.00')#initial display of string
    root.config(background = "lavender")
    
    fontstyle = TkFont.Font(family ="Helvetica",size = 60,)
    tk.Label(root,textvariable=txt_var,font=fontstyle,).pack()
    
    #creating the buttons for start,stop and reset
    tk.Button(root,text = "Start",command=start,bg ='misty rose').pack(fill = 'x')
    tk.Button(root,text='Stop',command = stop,bg ='misty rose').pack(fill='x')
    tk.Button(root,text = 'Reset',command = reset,bg ='misty rose').pack(fill='x')
    root.mainloop()
    
