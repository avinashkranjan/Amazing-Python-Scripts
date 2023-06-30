from datetime import datetime
import tkinter as tk
import tkinter.messagebox 
import pytz

#Creating main Window  
window = tk.Tk()
window.title("Time-Zone Converter")
window.geometry('480x300')

# giving the format of datetime
format = "%Y-%m-%d %H:%M"

#entry box for all the values
entry_cur_tz = tk.Entry(window, width=20, font=('arial',10))
entry_cur_tz.place(x=20,y=100)

entry_cnv_tz = tk.Entry(window, width=20, font=('arial',10))
entry_cnv_tz.place(x=250,y=100)

entry_cur_tm = tk.Entry(window, width=20, font=('arial',10))
entry_cur_tm.place(x=20,y=170)

entry_cnv_tm = tk.Entry(window, width=20, font=('arial',10))
entry_cnv_tm.place(x=250,y=170)

#All Entry Box configuration
def on_focus_in_ent_cur_tz(event):
    if entry_cur_tz.get() == 'Eg. Asia/Kolkata':
        entry_cur_tz.delete(0, "end")
        entry_cur_tz.insert(0, '')
        entry_cur_tz.config(fg = 'black')
def on_focus_out_ent_cur_tz(event):
    if entry_cur_tz.get() == '':
        entry_cur_tz.insert(0, 'Eg. Asia/Kolkata')
        entry_cur_tz.config(fg = 'grey')
        
entry_cur_tz.insert(0, 'Eg. Asia/Kolkata')
entry_cur_tz.bind('<FocusIn>', on_focus_in_ent_cur_tz)
entry_cur_tz.bind('<FocusOut>', on_focus_out_ent_cur_tz)
entry_cur_tz.config(fg = 'grey')


def on_focus_in_ent_cnv_tz(event):
    if entry_cnv_tz.get() == 'Eg. Australia/Sydney':
        entry_cnv_tz.delete(0, "end")
        entry_cnv_tz.insert(0, '')
        entry_cnv_tz.config(fg = 'black')
def on_focus_out_ent_cnv_tz(event):
    if entry_cnv_tz.get() == '':
        entry_cnv_tz.insert(0, 'Eg. Australia/Sydney')
        entry_cnv_tz.config(fg = 'grey')
        
entry_cnv_tz.insert(0, 'Eg. Australia/Sydney')
entry_cnv_tz.bind('<FocusIn>', on_focus_in_ent_cnv_tz)
entry_cnv_tz.bind('<FocusOut>', on_focus_out_ent_cnv_tz)
entry_cnv_tz.config(fg = 'grey')


def on_focus_in_ent_cur_tm(event):
    if entry_cur_tm.get() == "Eg. 2023-06-02 20:01":
        entry_cur_tm.delete(0, "end")
        entry_cur_tm.insert(0, '')
        entry_cur_tm.config(fg = 'black')
def on_focus_out_ent_cur_tm(event):
    if entry_cur_tm.get() == '':
        entry_cur_tm.insert(0, "Eg. 2023-06-02 20:01")
        entry_cur_tm.config(fg = 'grey')
        
entry_cur_tm.insert(0, "Eg. 2023-06-02 20:01")
entry_cur_tm.bind('<FocusIn>', on_focus_in_ent_cur_tm)
entry_cur_tm.bind('<FocusOut>', on_focus_out_ent_cur_tm)
entry_cur_tm.config(fg = 'grey')


def on_focus_in_ent_cnv_tm(event):
    if entry_cnv_tm.get() == 'Click convert button':
        entry_cnv_tm.delete(0, "end")
        entry_cnv_tm.insert(0, '')
        entry_cnv_tm.config(fg = 'black')
def on_focus_out_ent_cnv_tm(event):
    if entry_cnv_tm.get() == '':
        entry_cnv_tm.insert(0, 'Click convert button')
        entry_cnv_tm.config(fg = 'grey')
        
entry_cnv_tm.insert(0, 'Click convert button')
entry_cnv_tm.bind('<FocusIn>', on_focus_in_ent_cnv_tm)
entry_cnv_tm.bind('<FocusOut>', on_focus_out_ent_cnv_tm)
entry_cnv_tm.bind("<Key>", lambda a: "break")
entry_cnv_tm.config(fg = 'grey')


#All label with text
title_lbl=tk.Label(master=window,text="Time-Zone Converter",font=("broadway", 25),bg="black",fg='white')
title_lbl.place(x=48,y=10)

cur_tz_lbl=tk.Label(master=window,text="Current timezone name",font=("Times Roman", 10),fg='black')
cur_tz_lbl.place(x=16,y=80)
cnv_tz_lbl=tk.Label(master=window,text="Convert timezone name",font=("Times Roman", 10),fg='black')
cnv_tz_lbl.place(x=246,y=80)

cur_tm_lbl=tk.Label(master=window,text="Current time (YYYY-MM-DD H:M)",font=("Times Roman", 10),fg='black')
cur_tm_lbl.place(x=16,y=150)
cnv_tm_lbl=tk.Label(master=window,text="Converted time (YYYY-MM-DD H:M)",font=("Times Roman", 10),fg='black')
cnv_tm_lbl.place(x=246,y=150)

#Convert button function
def cnv_time():
 date_input = True

 #Check all the data is entered or not
 if entry_cur_tz.get() == 'Eg. Asia/Kolkata' or entry_cnv_tz.get() == 'Eg. Australia/Sydney' or entry_cur_tm.get() == 'Eg. 2023-06-02 20:01' or entry_cnv_tm == 'Click convert button':
     tkinter.messagebox.showerror(title="Error", message="Invalid inputs")
 #Check the date input format     
 elif entry_cur_tm.get() != 'Eg. 2023-06-02 20:01':
     try:
         my_timestamp = datetime.strptime(entry_cur_tm.get(), '%Y-%m-%d %H:%M')
     except ValueError:
         date_input = False
         tkinter.messagebox.showerror(title="Error", message="Invalid Date input")
 #Check if timezone entered is right or wrong and convert the date         
 if entry_cur_tz != 'Eg. Asia/Kolkata' and entry_cnv_tz != 'Eg. Australia/Sydney':
     try:
         if date_input == True:
             date_time = datetime.strptime(entry_cur_tm.get(), '%Y-%m-%d %H:%M')
             org_timezone = pytz.timezone(entry_cur_tz.get())
             new_timezone = pytz.timezone(entry_cnv_tz.get())
             org_timestamp = org_timezone.localize(date_time)
             new_timestamp = org_timestamp.astimezone(new_timezone)
             entry_cnv_tm.delete(0, "end")
             entry_cnv_tm.config(fg = 'black')
             entry_cnv_tm.insert(0, new_timestamp.strftime(format))
     except pytz.exceptions.UnknownTimeZoneError:
         tkinter.messagebox.showerror(title="Error", message="Invalid timezone input")         

# Convert Button     
button_cnv = tk.Button(window, text="Convert", width=10, command=cnv_time)
button_cnv.place(x=20,y=210)

window.resizable(False, False) 
window.mainloop()
