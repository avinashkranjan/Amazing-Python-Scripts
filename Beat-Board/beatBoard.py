from tkinter import *
from playsound import playsound
from threading import Thread


class padSound:
    def __init__(self, soundLocation):
        self.soundLocation = soundLocation

    def given_sound(self):
        playsound(self.soundLocation)

    # def play_sound(event):
    #     sound = Thread(target=given_sound)
    #     sound.start()

kickLocation  = 'Beat-Board/Sounds/Kick_Muffled.wav'
hiHatLocation = 'Beat-Board/Sounds/Hi-Hat-Closed-Hit-A1-www.fesliyanstudios.com.wav'
snareLocation = 'Beat-Board/Sounds/SnareToTape.wav'
pad1Location  = 'Beat-Board/Sounds/Pad1.wav'
pad2Location  = 'Beat-Board/Sounds/Pad2.wav'
pad3Location  = 'Beat-Board/Sounds/Pad3.wav'
pad4Location  = 'Beat-Board/Sounds/Pad4.wav'
pad5Location  = 'Beat-Board/Sounds/Pad5.wav'
pad6Location  = 'Beat-Board/Sounds/Pad6.wav'

kickDrum  = padSound(kickLocation)
hiHatDrum = padSound(hiHatLocation)
snareDrum = padSound(snareLocation)

pad1 = padSound(pad1Location)
pad2 = padSound(pad2Location)
pad3 = padSound(pad3Location)
pad4 = padSound(pad4Location)
pad5 = padSound(pad5Location)
pad6 = padSound(pad6Location)


# ============ KICK ==================

# def kick_sound():
#     playsound('Beat-Board/Sounds/Kick_Muffled.wav')


# def play_kick(event):
#     sound1 = Thread(target=kick_sound)
#     sound1.start()

def play_kick(event):
    sound = Thread(target=kickDrum.given_sound)
    sound.start()


# ======================================

# ============ HI-HAT ==================

# def hihat_sound():
#     playsound('Beat-Board/Sounds/Hi-Hat-Closed-Hit-A1-www.fesliyanstudios.com.wav')


# def play_hat(event):
#     sound2 = Thread(target=hihat_sound)
#     sound2.start()

def play_hat(event):
    sound2 = Thread(target=hiHatDrum.given_sound)
    sound2.start()


# =====================================

# ============ SNARE ==================

# def snare_sound():
#     playsound('Beat-Board/Sounds/SnareToTape.wav')


# def play_snare(event):
#     sound3 = Thread(target=snare_sound)
#     sound3.start()

def play_snare(event):
    sound3 = Thread(target=snareDrum.given_sound)
    sound3.start()


# =====================================

# ============ PAD 1 ==================

# def pad1_sound():
#     playsound('Beat-Board/Sounds/Pad1.wav')


# def play_pad1(event):
#     sound4 = Thread(target=pad1_sound)
#     sound4.start()

def play_pad1(event):
    sound4 = Thread(target=pad1.given_sound)
    sound4.start()


# =====================================

# ============ PAD 2 ==================

# def pad2_sound():
#     playsound('Beat-Board/Sounds/Pad2.wav')


# def play_pad2(event):
#     sound5 = Thread(target=pad2_sound)
#     sound5.start()

def play_pad2(event):
    sound5 = Thread(target=pad2.given_sound)
    sound5.start()


# =====================================

# ============ PAD 3 ==================

# def pad3_sound():
#     playsound('Beat-Board/Sounds/Pad3.wav')


# def play_pad3(event):
#     sound6 = Thread(target=pad3_sound)
#     sound6.start()

def play_pad3(event):
    sound6 = Thread(target=pad3.given_sound)
    sound6.start()


# =====================================

# ============ PAD 4 ==================

# def pad4_sound():
#     playsound('Beat-Board/Sounds/Pad4.wav')


# def play_pad4(event):
#     sound7 = Thread(target=pad4_sound)
#     sound7.start()

def play_pad4(event):
    sound7 = Thread(target=pad4.given_sound)
    sound7.start()

# =====================================

# ============ PAD 5 ==================

# def pad5_sound():
#     playsound('Beat-Board/Sounds/Pad5.wav')


# def play_pad5(event):
#     sound8 = Thread(target=pad5_sound)
#     sound8.start()

def play_pad5(event):
    sound8 = Thread(target=pad5.given_sound)
    sound8.start()


# =====================================

# ============ PAD 6 ==================
# def pad6_sound():
#     playsound('Beat-Board/Sounds/Pad6.wav')


# def play_pad6(event):
#     sound9 = Thread(target=pad6_sound)
#     sound9.start()

def play_pad6(event):
    sound9 = Thread(target=pad6.given_sound)
    sound9.start()


# =====================================
def create_layout():

    # Creates the Frame
    frame_a = Frame(master=main_window, width=500, height=500, bg="black")
    frame_a.grid(rowspan=3, columnspan=3)
    frame_a.focus_set()

# Creates the Buttons
# ------------------------------------------------
    # Kick Button
    kick = Button(text="Kick", height=5, width=10)
    frame_a.bind('q', play_kick)
    kick.bind("<Button-1>", play_kick)

    # frame_a.bind('q', kickDrum.play_sound)
    # kick.bind("<Button-1>", kickDrum.play_sound)

    # Hi-hat Button
    hihat = Button(text="Hi-Hat", height=5, width=10)
    frame_a.bind('w', play_hat)
    hihat.bind("<Button-1>", play_hat)

    # Snare Button
    snare = Button(text="Snare", height=5, width=10)
    frame_a.bind('e', play_snare)
    snare.bind("<Button-1>", play_snare)

# -------------------------------------------------
    # Pad 1
    pad1 = Button(text="Pad 1", height=5, width=10)
    frame_a.bind('a', play_pad1)
    pad1.bind("<Button-1>", play_pad1)

    # Pad 2
    pad2 = Button(text="Pad 2", height=5, width=10)
    frame_a.bind('s', play_pad2)
    pad2.bind("<Button-1>", play_pad2)

    # Pad 3
    pad3 = Button(text="Pad 3", height=5, width=10)
    frame_a.bind('d', play_pad3)
    pad3.bind("<Button-1>", play_pad3)

# -------------------------------------------------
    # Pad 4
    pad4 = Button(text="Pad 4", height=5, width=10)
    frame_a.bind('z', play_pad4)
    pad4.bind("<Button-1>", play_pad4)

    # Pad 5
    pad5 = Button(text="Pad 5", height=5, width=10)
    frame_a.bind('x', play_pad5)
    pad5.bind("<Button-1>", play_pad5)

    # Pad 6
    pad6 = Button(text="Pad 6", height=5, width=10)
    frame_a.bind('c', play_pad6)
    pad6.bind("<Button-1>", play_pad6)

# -------------------------------------------------

    # Display Buttons
    kick.grid(row=0)
    hihat.grid(row=0, column=1)
    snare.grid(row=0, column=2)

    pad1.grid(row=1)
    pad2.grid(row=1, column=1)
    pad3.grid(row=1, column=2)

    pad4.grid(row=2)
    pad5.grid(row=2, column=1)
    pad6.grid(row=2, column=2)


main_window = Tk()
main_window.resizable(False,False)
main_window.title('Sound Board')
create_layout()
main_window.mainloop()
