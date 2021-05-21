import time
import tkinter as tk
from tkinter import messagebox
import pygame
from datetime import timedelta

pygame.mixer.init()
pomo_count = 0
break_count = 0

# path of host file in windows
host_path = r"C:\Windows\System32\drivers\etc\hosts"

# URL of websites to block
block_list = [
    'www.facebook.com', 'facebook.com',
    'www.youtube.com', 'youtube.com',
    'www.gmail.com', 'gmail.com',
    'www.instagram.com', 'instagram.com',
    'www.twitter.com', 'twitter.com'
]

# redirecting above URLs to this localhost to ensure blocking
redirect = "127.0.0.1"

def block_websites():
    """
    The function will open the host file and add the block-list websites to
    the file if it is not already present and redirect it to the localhost
    for blocking
    """

    try:
        # Opening the host file in reading and writing mode
        with open(host_path, 'r+') as h_file:
            content = h_file.read()

            for website in block_list:

                # Website is already blocked
                if website in content:
                    pass

                # To redirect the website to be blocked
                else:
                    h_file.write(redirect + "\t" + website + "\n")

    except PermissionError:
        tk.messagebox.showinfo("Error", "Run cmd in the admin mode and then try again!\nDeselect the option to prevent this popup to show again.")

    except (FileNotFoundError, NameError):
        tk.messagebox.showinfo("Error", "Functionality not supported in your OS!\nDeselect the option to prevent this popup to show again.")


def remove_websites():
    """
    The function will unblock the block_list websites by opening the file
    and removing the changes we made before
    """
    try:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                if not any(website in lines for website in block_list):
                    file.write(lines)
            file.truncate()
    except:
        pass
    finally:
        pass


def high_focus():
    global enable
    if enable.get() == 1:
        block_websites()
    else:
        remove_websites()


def break_timer():
    global popup_2
    popup_2 = tk.Toplevel(root)
    popup_2.title("Break Timer!")
    popup_2.geometry("370x120")
    round = 0

    try:
        t = 5*60
        while t>-1:
            minute_count = t // 60
            second_count = t % 60
            timer = '{:02d}:{:02d}'.format(minute_count, second_count)
            time_display = tk.Label(popup_2, text = timer, bg = 'DodgerBlue4', fg = 'white', font = ('STIX', 90, 'bold'))
            time_display.place(x=0,y=0)
            popup_2.update()
            time.sleep(1)
            t -= 1
    except:
        pass    

    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play(loops=0)

    if t == -1:
        tk.messagebox.showinfo("Time's up!", "Break is over!\nTime to get to work!")
        popup_2.destroy()
        global break_count
        break_count += 1
    

def show_report():
    global popup_3
    popup_3 = tk.Toplevel(root)
    popup_3.title("Report")
    popup_3.geometry("370x170")
    popup_3.config( bg = 'DodgerBlue4')

    pomo_time = str(timedelta(minutes=pomo_count*25))[:-3]
    break_time = str(timedelta(minutes=pomo_count*5))[:-3]
    tk.Label(popup_3, text=f"Number of Pomodoros completed: {pomo_count}", justify=tk.LEFT, bg = 'DodgerBlue4', fg = 'white', font=('Arial',12,'bold')).place(x = 10, y = 10)
    tk.Label(popup_3, text=f"Number of breaks completed: {break_count}", justify=tk.LEFT, bg = 'DodgerBlue4', fg = 'white', font=('Arial',12,'bold')).place(x = 10, y = 50)
    tk.Label(popup_3, text=f"Hours of work done: {pomo_time} hrs", justify=tk.LEFT,  bg = 'DodgerBlue4', fg = 'white', font=('Arial',12,'bold')).place(x = 10, y = 90)
    tk.Label(popup_3, text=f"Hours of break taken: {break_time} hrs", justify=tk.LEFT,  bg = 'DodgerBlue4', fg = 'white', font=('Arial',12,'bold')).place(x = 10, y = 130)


def pomodoro_timer():
    global popup_1
    popup_1 = tk.Toplevel(root)
    popup_1.title("Work Timer!")
    popup_1.geometry("370x120")
    round = 0

    try:
        t = 25*60
        while t>-1:
            minute_count = t // 60
            second_count = t % 60
            timer = '{:02d}:{:02d}'.format(minute_count, second_count)
            time_display = tk.Label(popup_1, text = timer, bg = 'DodgerBlue4', fg = 'white', font = ('STIX', 90, 'bold'))
            time_display.place(x=0,y=0)
            popup_1.update()
            time.sleep(1)
            t -= 1
    except:
        pass    

    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play(loops=1)

    if t == -1:
        tk.messagebox.showinfo("Time's up!", "Pomodoro completed successfully!\nYou deserve a break!")
        popup_1.destroy()
        global pomo_count
        pomo_count += 1


def main():
    global root
    root = tk.Tk()
    root.title('Timer')
    root.geometry('470x608')

    bg = tk.PhotoImage(file = "bg.png")
    
    # Show image using label
    label1 = tk.Label( root, image = bg)
    label1.place(x = 0, y = 0)

    global count

    intro1 = tk.Label(root, text = 'POMODORO TIMER', bg = 'snow', fg = 'maroon', font = ('Arial', 25, 'bold'))
    intro1.place(x=100, y=120)

    global enable
    enable = tk.IntVar()
    check  = tk.Checkbutton(root, text = 'Enable website blocker', variable = enable, font = ('Arial', 12, 'bold'), bg='gold', activebackground='yellow', height = 1, width = 25, onvalue=1, offvalue=0, command=high_focus)
    check.place(x=100, y=190)

    start_btn = tk.Button(root, text = 'START WORK TIMER', command = pomodoro_timer, font = ('Arial', 12, 'bold'), bg='gold', activebackground='yellow', height = 3, width = 25)
    start_btn.place(x=100, y=250)

    break_btn = tk.Button(root, text = 'START BREAK TIMER', command = break_timer, font = ('Arial', 12, 'bold'), bg='gold', activebackground='yellow', height = 3, width = 25)
    break_btn.place(x=100, y=350)

    report_btn = tk.Button(root, text = 'SHOW REPORT', command = show_report, font = ('Arial', 12, 'bold'), bg='gold', activebackground='yellow', height = 3, width = 25)
    report_btn.place(x=100, y=450)

    root.mainloop()


if __name__ == '__main__':
	main()

