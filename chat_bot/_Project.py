"""

Project Name : ChatBot

Developer : Varshith.G

Description :
    A simple chatbot which reads the text files provided to it and gives answers accordingly.
If it does not answer the question u have asked than u can feed any answer for your question.
The answer u have feeded will be stored in the file automatically for later use.

Problems :
    -> It can not answer any question which is not present in the file which is fed into it.  
    -> It would give u an error if u will write the last line of the file as question.

Use your own files :
    U can use your own files but following things should be done carefully :
    -> The file should have ".txt" extension.
    -> Question should be entered on one line without any spaces.
    -> Answer should be on the very next line of the question. Write the answer in the way u want to display it.

"""

"""
importing all required
        modules
"""


# ------------------------------------------------------------------------------------------

"""  colors  for   later   use"""

import time
import tkinter
from tkinter import *
c1 = '#263238'
c2 = '#faa21f'
c3 = '#1e282d'
c6 = '#577e75'

c4 = '#faa21f'
c5 = '#577e75'

c7 = '#1e282d'
c8 = '#faa21f'

# Alternative Chat Colours
'''
c4 = '#4790f9'
c5 = '#00a3cf'

c7 = '#85c0f6'
c8 = '#83e7f2'
'''

# -------------------------------------------------------------------------------------------

"""
getting data from entry of
    'Enter Name' page
"""


def info():

    global myname
    myname = entry_user.get('1.0', 'end-1c')

    global chatbot
    chatbot = entry_chat.get('1.0', 'end-1c')

    if myname == "" or chatbot == "":
        Label(frame_info, text="Fill both fields to proceed.", bg="red",
              fg="white", font='Verdana 11 bold').place(x=182, y=96)
        return

    entry_user.delete('1.0', END)
    entry_chat.delete('1.0', END)

    frame_info.pack_forget()
    frame_topic.pack()

# ------------------------------------------------------------------------------------------


"""
opening files after selection of
        topic in topic selestion
                    page
"""


def topic_1():
    global no_topic
    no_topic = 1

    global top
    top = 'd1_technology.txt'

    global a
    a = open(top, 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget()
    frame_chat.pack()

    topic = 'Technology'
    label_topic.config(text=topic)

    refresh_screen()

# ----------------------------------------------------------------------------------------------------------


"""
functions for writing in files
        for writing in files in chat screen

"""


def write_ans():

    enter1 = entry_feed.get('1.0', END)

    b.write(enter1)
    b.close()

    window.destroy()

    """           
        Reopening of files after
           changes are saved
    """

    if no_topic == 1:
        topic_1()


def feed_answer():
    """
a seperate window for writing answer
            on file

    """

    global window
    window = Tk()

    frame_root = Frame(window, bg=c1)
    frame_root.pack()

    label = Label(
        frame_root, text='Enter the answer of Question here ...', bg=c1, fg='white')
    label.pack()

    global entry_feed
    entry_feed = Text(frame_root, height=6, width=30, fg='white', bg=c2)
    entry_feed.bind('<Return>', write_ans)
    entry_feed.pack()

    button = Button(frame_root, text='Add answer',
                    command=write_ans, bg=c3, fg='white')
    button.pack()


def write_file():
    """
opening file for appending in
exsisting  files

    """
    global b
    b = open(top, 'a')

    b.write(chat_raw)
    b.write('\n')

    button_write.place_forget()
    feed_answer()

# ----------------------------------------------------------------------------------------------


def refresh_screen():

    for widget in frame_chats.winfo_children():
        widget.destroy()

    button_write.place_forget()
    label_space = Label(frame_chats, bg=c1,  text='')
    label_space.pack()

# ------------------------------------------------------------------------------------------


def submit():
    """
function for producing response of
        request of user

    """

    button_write.place_forget()
    global chat_raw
    chat_raw = entry.get('1.0', 'end-1c')

    entry.delete('1.0', END)

    chat = chat_raw.lower()
    chat = chat.replace(' ', '')

    global label_request
    label_request = Label(frame_chats, text=chat_raw, bg=c4, fg=c7,
                          justify=LEFT, wraplength=300, font='Verdana 10 bold')

    label_request.pack(anchor='w')

    global answer

    if chat == 'whodevelopedyou?' or chat == 'whoinventedyou?' or chat == 'developer' or chat == 'whoisyourgod?':
        answer = "Varshith"

    elif chat == "what'smyname?" or chat == "whatsmyname?" or chat == "whatismyname?" or chat == "whatsmyname" or chat == 'myname?' or chat == 'myname':
        answer = myname

    elif chat == "what'syourname?" or chat == "whatisyourname?" or chat == "whatsyourname?" or chat == "whatsyourname" or chat == 'yourname?' or chat == 'yourname':
        answer = chatbot

    elif chat == 'bye' or chat == 'goodbye' or chat == 'exit' or chat == 'close' or chat == 'end':
        answer = 'Bye'

    else:
        i = 0
        j = 0
        for lines in doc:
            stats = lines[:-1]
            stats = stats.lower()
            stat = stats.replace(' ', '')
            i += 1
            if stat == chat:
                answer = doc[i]
                break
            else:
                j += 1

        if i == j:
            answer = "I don't understand.........please teach me ! "
            button_write.place(x=430, y=3)

    get_response()


def get_response():

    global label_response
    label_response = Label(frame_chats, text=answer, bg=c5, fg=c8,
                           justify=LEFT, wraplength=300, font='Verdana 10 bold')

    label_response.pack(anchor='e')

    if answer == 'Bye':
        root.destroy()


# ------------------------------------------------------------------------------------------------------------------

"""

moving from one page to another
    by help of button

"""


def welcome_to_info():
    frame_welcome.pack_forget()
    frame_info.pack()


def info_to_topic():
    frame_info.pack_forget()
    frame_topic.pack()


def topic_to_chat():
    frame_topic.pack_forget()
    frame_chat.pack()


def chat_to_topic():
    frame_chat.pack_forget()
    frame_topic.pack()


def topic_to_info():
    frame_topic.pack_forget()
    frame_info.pack()


def info_to_welcome():
    frame_info.pack_forget()
    frame_welcome.pack()


# -----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
"""
calling constructor to make window

"""

root = Tk()

# ----------------------------------------------------------------------------------------------------

"""  images used in window  """

back = PhotoImage(file='arrow_behind.png')

front = PhotoImage(file='arrow_ahead.png')

exitt = PhotoImage(file='exit.png')

screen_1 = PhotoImage(file='image_5.png')

submit_img = PhotoImage(file='image_8.png')

submit_img = PhotoImage(file='image_8.png')
# ---------------------------------------------------------------------------------------------------------------------

"""     WELCOME FRAME    """
"""    first frame containing time date and welcome messages """

frame_welcome = Frame(root, bg=c1, height='670', width='550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()


welcome = Label(frame_welcome, text='Welcome',
                font="Vardana 40 bold", bg=c1, fg="white")
welcome.place(x=160, y=200)

welcome_chatbot = Label(frame_welcome, text='I am Chatbot ! ',
                        font="Helvetica 15 bold italic", bg=c1, fg=c6)
welcome_chatbot.place(x=200, y=270)

welcome_chatbot = Label(frame_welcome, text='Designed by VARSHITH ',
                        font="Helvetica 8 bold", bg=c1, fg='white')
welcome_chatbot.place(x=415, y=340)

pic_1 = Label(frame_welcome, image=screen_1)
pic_1.place(x=-3, y=357)

button_front = Button(frame_welcome, image=front, relief="flat", bg=c1,
                      bd="3px solid black", command=welcome_to_info).place(x=470, y=10)

# __________________________________________________________________

"""  time option  """


def clock():
    current = time.strftime("%H:%M:%S")
    label_time = Label(frame_welcome, bd=5,  text=current, height=1,
                       width=8, font='Ariel 11 bold',  fg="white", relief='groove', bg=c3)
    label_time.place(x=120, y=63)

    label_time.after(1000, clock)


button_time = Button(frame_welcome, text='Time', height=1,
                     font='Vardana 10 bold',  width=8, bg=c2, fg=c1,  command=clock)
button_time.place(x=30, y=63)

# _____________________________________________________________________________________________________________________

"""    date option   """


def date():

    try:
        date = time.strftime("%d %B , 20%y")
        label_date = Label(frame_welcome, bd=5, relief='groove',
                           text=date, bg=c3, fg="white", height=1, font='Ariel 11 bold')
        label_date.place(x=400, y=63)

        label_date.after(86400000, date)

    except AttributeError:
        print('')


button_date = Button(frame_welcome, text='Date', height=1,
                     font='Vardana 10 bold',  width=8, bg=c2, fg=c1, command=date)
button_date.place(x=310, y=63)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""     INFO FRAME   """
"""     frame of entering names    """

frame_info = Frame(root, bg=c1, height='670', width='550')
frame_info.pack_propagate(0)

spacer1 = Label(frame_info, bg=c1)
spacer1.pack()

spacer2 = Label(frame_info, bg=c1)
spacer2.pack()

label_sub = Label(frame_info, text="Enter Information",
                  bg=c1, fg="white", font='Verdana 30')
label_sub.pack()

user_name = Label(frame_info, text='Enter your name : ',
                  bg=c1, fg=c2, font='Ariel 15')
user_name.place(x=80, y=130)

entry_user = Text(frame_info, bg=c6, fg="white",
                  height='1', width='40', font='Ariel 15')
entry_user.focus()
entry_user.place(x=80, y=170)

chatbot_name = Label(
    frame_info, text='Give a name to your Assistant : ', bg=c1, fg=c2, font='Ariel 15')
chatbot_name.place(x=80, y=220)

entry_chat = Text(frame_info, bg=c6, fg="white",
                  height='1', width='40', font='Ariel 15')
entry_chat.place(x=80, y=260)

button_1 = Button(frame_info, text='submit',
                  font='Vardana 10 bold', bg=c2, fg=c1, command=info)
button_1.place(x=470, y=330)

designer_name = Label(
    frame_info, text='Designed by VARSHITH', bg=c1, fg='white')
designer_name.place(x=420, y=650)

button_back = Button(frame_info, image=back, relief="flat",
                     bg=c1, command=info_to_welcome).place(x=10, y=10)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""     TOPIC FRAME   """
""""   frame for topic selection     """

frame_topic = Frame(root, bg=c1, height='670', width='550')
frame_topic.pack_propagate(0)

spacer3 = Label(frame_topic, bg=c1)
spacer3.pack()

spacer4 = Label(frame_topic, bg=c1)
spacer4.pack()

select_label = Label(frame_topic, text="Select Topic",
                     bg=c1, fg="white", font='Ariel 30 italic')
select_label.pack()

spacer5 = Label(frame_topic, bg=c1)
spacer5.pack()

option_1 = Label(frame_topic, text='1- Technology',
                 font='Verdana 15 italic', bg=c1, fg=c2)
option_1.place(x=30, y=120)

button_opt_1 = Button(frame_topic, text='Proceed',
                      image=front, relief="flat", bg=c1, command=topic_1)
button_opt_1.place(x=350, y=120)

option_2 = Label(frame_topic, text='Designed by VARSHITH',
                 font='Verdana 8', bg=c1, fg='white')
option_2.place(x=410, y=650)
button_back = Button(frame_topic, image=back, relief="flat",
                     bg=c1, command=topic_to_info).place(x=10, y=10)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""         CHAT FRAME   """
""""       main chat screen   """

frame_chat = Frame(root, bg=c1, height='670', width='550')
frame_chat.pack_propagate(0)

frame_top = Frame(frame_chat, bg=c3, height='100', width='550')
frame_top.pack()

label_topic = Label(frame_top, bg=c3, fg='white', font='Verdana 20 bold ')
label_topic.pack(pady='40')

frame_spacer = Frame(frame_top, bg=c2, height="10", width="550")
frame_spacer.pack()

bottom_frame = Frame(frame_chat, bg=c2, height='90', width='550')
bottom_frame.pack_propagate(0)
bottom_frame.pack(side=BOTTOM)

button = Button(bottom_frame, image=submit_img,
                font='Vardana 8 bold', bg=c3, command=submit)
button.place(x=410, y=27)

entry = Text(bottom_frame, bg=c3, fg='white', relief="flat",
             height='4', width='45', font='Verdana 10')
entry.bind('<Return>', submit)
entry.place(x=10, y=9)

frame_chats = Frame(frame_chat, bg='white', height='450', width='500')
frame_chats.pack_propagate(0)
frame_chats.pack()

label_space = Label(frame_chats, bg='white').pack()

button_refresh = Button(frame_chat, bg=c3, fg=c2,  text='refresh',
                        font='Vardana 10 bold',  command=refresh_screen)
button_refresh.place(x=440, y=80)

button_write = Button(bottom_frame, text=' write here !', width=15,
                      bg='black', fg='white', font='Vardana 8',  command=write_file)

button_back = Button(frame_chat, image=back, relief="flat",
                     bg=c3, command=chat_to_topic).place(x=10, y=10)
button_front = Button(frame_chat, image=exitt, relief="flat",
                      bg=c3, command=root.destroy).place(x=440, y=10)

# -----------------------------------------------------------------------------------------------------------
root.mainloop()
"""    END OF CODE relief = "flat",  """
