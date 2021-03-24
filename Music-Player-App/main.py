from tkinter import *
import os
import time
import threading
from mutagen.mp3 import MP3
from tkinter import filedialog
import tkinter.messagebox
from tkinter import ttk  # to improve the styles of buttons and widgets
from ttkthemes import themed_tk as tk
from pygame import mixer


def show_Details(play_it):
    Main_text['text'] = 'Playing.....' + ' ' + os.path.basename(play_it)
    Main_text['anchor'] = 'e'
    file_ext = os.path.splitext(play_it)
    if file_ext[1] == '.mp3':  # To handle mp3 files using mutagen
        audio_lenth = MP3(play_it)
        total_lenth = audio_lenth.info.length
    else:  # to handle .wav,.ogg music file extensions
        a = mixer.Sound(play_it)
        total_lenth = a.get_length()

    m, s = divmod(total_lenth, 60)
    m = round(m)
    s = round(s)

    time_format = '{:02d}:{:02d}'.format(m, s)
    Main_lenth['text'] = 'Duration : '+' '+time_format
    thread1 = threading.Thread(target=rem_count, args=(total_lenth,))
    thread1.start()


def rem_count(total_lenth):
    global paused
    curr_secs = 0
    while curr_secs <= total_lenth and mixer.music.get_busy():
        if paused:
            continue
        else:
            m, s = divmod(curr_secs, 60)
            m = round(m)
            s = round(s)
            m1, s1 = divmod(total_lenth, 60)
            m1 = round(m1)
            s1 = round(s1)

            time_format = '{:02d}:{:02d}'.format(m, s)
            time_format1 = '{:02d}:{:02d}'.format(m1, s1)
            current_lenth['text'] = 'Cuurent Duration : ' + ' ' + time_format
            time.sleep(1)
            curr_secs += 1
            total_lenth -= 1


def Play_music():
    global paused
    if paused:
        mixer.music.unpause()
        # global paused = FALSE
        status_bar['text'] = 'Playing Music.....' + \
            ' ' + os.path.basename(music_file)
        status_bar['anchor'] = 'w'
        paused = FALSE
    else:
        try:
            Stop_music()
            time.sleep(1)
            song = play_list.curselection()
            song = int(song[0])
            play_it = music_list[song]

            mixer.music.load(play_it)
            mixer.music.play()
            status_bar['text'] = 'Playing Music.....' + \
                ' ' + os.path.basename(play_it)
            status_bar['anchor'] = 'w'
            show_Details(play_it)
        except:
            tkinter.messagebox.showerror("Error", "File Not Selected")


def Stop_music():
    mixer.music.stop()
    status_bar['text'] = 'Music Stopped'
    status_bar['anchor'] = 'e'


paused = FALSE


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    status_bar['text'] = 'Music Paused...'
    status_bar['anchor'] = 'e'


def rewind_music():
    Play_music()
    status_bar['text'] = 'Music Rewinded...'+' '+os.path.basename(music_file)
    status_bar['anchor'] = 'e'


def close_window_fully():
    Stop_music()
    exit()


def set_vol(val):
    vol = float(val)/100
    mixer.music.set_volume(vol)


def about_us():
    tkinter.messagebox.showinfo(
        'About Rockerz', 'This Is A Music Player Devloped With Python Tkinter And Pygame By Robin Singh')


def browse_files():
    global music_file
    music_file = filedialog.askopenfilename()
    add_to_listbox(music_file)


music_list = []


def add_to_listbox(music_file):
    file_name = os.path.basename(music_file)
    index = 0
    play_list.insert(index, file_name)
    music_list.insert(index, music_file)
    play_list.pack()
    index += 1


def delete_btn():
    song = play_list.curselection()
    song = int(song[0])
    play_list.delete(song)
    music_list.pop(song)


def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(.7)
        vol_button1.configure(image=pic5)
        scale1.set(70)
        muted = FALSE

    else:
        mixer.music.set_volume(0)
        vol_button1.configure(image=pic4)
        scale1.set(0)
        muted = TRUE


def close_window_fully1():
    Stop_music()
    exit()


muted = FALSE


main_window = tk.ThemedTk()
main_window.get_themes()
# themes : 'arc','radiance','breeze','ubuntu' etc
main_window.set_theme("breeze")
# creating toolbar
tool_bar = Menu(main_window)
main_window.config(menu=tool_bar)

status_bar = ttk.Label(main_window, text="Welcome To Rockerzz",
                       relief=SUNKEN, anchor=W, font='verdana 10 italic')
status_bar.pack(side=BOTTOM, fill=X)

# creating sub menus
sub_menu = Menu(tool_bar, tearoff=0)  # to remove dashed line from menu
tool_bar.add_cascade(label='File', menu=sub_menu)
sub_menu.add_command(label="Open", command=browse_files)
sub_menu.add_command(label="Exit", command=close_window_fully1)

sub_menu = Menu(tool_bar, tearoff=0)  # to remove dashed line from menu
tool_bar.add_cascade(label='Help', menu=sub_menu)
sub_menu.add_command(label="About Us ", command=about_us)


mixer.init()

# main_window.geometry("600x300")
main_window.title("Rockerz")
main_window.iconbitmap("./Music-Player-App/assests/rockerz.ico")

left_frame = Frame(main_window)
left_frame.pack(side=RIGHT, padx=30, pady=20)
play_list = Listbox(left_frame)
play_list.pack()


add_btn = ttk.Button(left_frame, text='ADD', command=browse_files)
add_btn.pack(side=LEFT, padx=3)

del_btn = ttk.Button(left_frame, text='DELETE', command=delete_btn)
del_btn.pack(side=LEFT)

right_frame = Frame(main_window)
right_frame.pack(pady=20)

r_top_frame = Frame(right_frame)
r_top_frame.pack()

Main_text = ttk.Label(
    r_top_frame, text="Devloped By Robin Singh", font='arial 10 italic')
Main_text.pack()

Main_lenth = ttk.Label(r_top_frame, text="Length : --:--", relief=GROOVE)
Main_lenth.pack(pady=5)

current_lenth = ttk.Label(
    r_top_frame, text="Current Duration : --:--", relief=GROOVE)
current_lenth.pack()

playlist_box = Listbox(main_window)
canvas = Frame(right_frame)
canvas.pack(pady=5)

pic = PhotoImage(file="./Music-Player-App/assests/images/play.png")
play_button1 = ttk.Button(canvas, image=pic, command=Play_music)
play_button1.grid(row=0, column=0, padx=5)

pic1 = PhotoImage(file="./Music-Player-App/assests/images/stop.png")
stop_button1 = ttk.Button(canvas, image=pic1, command=Stop_music)
stop_button1.grid(row=0, column=1, padx=5)

pic2 = PhotoImage(file="./Music-Player-App/assests/images/pause.png")
pause_button1 = ttk.Button(canvas, image=pic2, command=pause_music)
pause_button1.grid(row=0, column=2, padx=5)

bottom_canvas = Frame(right_frame)
bottom_canvas.pack(padx=30, pady=30)
pic3 = PhotoImage(file="./Music-Player-App/assests/images/rewind.png")
rewind_button1 = ttk.Button(bottom_canvas, image=pic3, command=rewind_music)
rewind_button1.grid(row=0, column=0, pady=10)

pic4 = PhotoImage(file="./Music-Player-App/assests/images/002-mute.png")
pic5 = PhotoImage(file="./Music-Player-App/assests/images/001-volume.png")
vol_button1 = ttk.Button(bottom_canvas, image=pic5, command=mute_music)
vol_button1.grid(row=0, column=1)


scale1 = ttk.Scale(bottom_canvas, from_=0, to=100,
                   orient=HORIZONTAL, command=set_vol)
scale1.set(50)
mixer.music.set_volume(.5)
scale1.grid(row=0, column=3, padx=5, pady=10)

# For overriding close button
main_window.protocol("WM_DELETE_WINDOW", close_window_fully)
main_window.mainloop()
