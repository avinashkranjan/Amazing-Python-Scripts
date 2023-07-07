from tkinter import *
from playsound import playsound
from threading import Thread


class padSound:
    def __init__(self, soundLocation):
        self.soundLocation = soundLocation

    def given_sound(self):
        playsound(self.soundLocation)

    def play_sound(self, event):
        sound = Thread(target=self.given_sound)
        sound.start()


# All the locations of the sounds
kickLocation = './Beat-Board/Sounds/Kick.wav'
hiHatLocation = './Beat-Board/Sounds/hiHat.wav'
snareLocation = './Beat-Board/Sounds/snare.wav'
pad1Location = './Beat-Board/Sounds/Pad1.wav'
pad2Location = './Beat-Board/Sounds/Pad2.wav'
pad3Location = './Beat-Board/Sounds/Pad3.wav'
pad4Location = './Beat-Board/Sounds/Pad4.wav'
pad5Location = './Beat-Board/Sounds/Pad5.wav'
pad6Location = './Beat-Board/Sounds/Pad6.wav'

# Create drum objects
kickDrum = padSound(kickLocation)
hiHatDrum = padSound(hiHatLocation)
snareDrum = padSound(snareLocation)

# Create pad objects
pad1 = padSound(pad1Location)
pad2 = padSound(pad2Location)
pad3 = padSound(pad3Location)
pad4 = padSound(pad4Location)
pad5 = padSound(pad5Location)
pad6 = padSound(pad6Location)


def create_layout():

    # Creates the Frame
    frame_a = Frame(master=main_window, width=500, height=500, bg="black")
    frame_a.grid(rowspan=3, columnspan=3)
    frame_a.focus_set()

    # Creates the Buttons
    # ------------------------------------------------
    # Kick Button
    kickButton = Button(text="Kick", height=5, width=10)
    frame_a.bind('q', kickDrum.play_sound)
    kickButton.bind("<Button-1>", kickDrum.play_sound)

    # Hi-hat Button
    hihatButton = Button(text="Hi-Hat", height=5, width=10)
    frame_a.bind('w', hiHatDrum.play_sound)
    hihatButton.bind("<Button-1>", hiHatDrum.play_sound)

    # Snare Button
    snareButton = Button(text="Snare", height=5, width=10)
    frame_a.bind('e', snareDrum.play_sound)
    snareButton.bind("<Button-1>", snareDrum.play_sound)

    # -------------------------------------------------
    # Pad 1
    pad1Button = Button(text="Pad 1", height=5, width=10)
    frame_a.bind('a', pad1.play_sound)
    pad1Button.bind("<Button-1>", pad1.play_sound)

    # Pad 2
    pad2Button = Button(text="Pad 2", height=5, width=10)
    frame_a.bind('s', pad2.play_sound)
    pad2Button.bind("<Button-1>", pad2.play_sound)

    # Pad 3
    pad3Button = Button(text="Pad 3", height=5, width=10)
    frame_a.bind('d', pad3.play_sound)
    pad3Button.bind("<Button-1>", pad2.play_sound)

    # -------------------------------------------------
    # Pad 4
    pad4Button = Button(text="Pad 4", height=5, width=10)
    frame_a.bind('z', pad4.play_sound)
    pad4Button.bind("<Button-1>", pad4.play_sound)

    # Pad 5
    pad5Button = Button(text="Pad 5", height=5, width=10)
    frame_a.bind('x', pad5.play_sound)
    pad5Button.bind("<Button-1>", pad5.play_sound)

    # Pad 6
    pad6Button = Button(text="Pad 6", height=5, width=10)
    frame_a.bind('c', pad6.play_sound)
    pad6Button.bind("<Button-1>", pad6.play_sound)
    # -------------------------------------------------

    # Display Buttons
    kickButton.grid(row=0)
    hihatButton.grid(row=0, column=1)
    snareButton.grid(row=0, column=2)

    pad1Button.grid(row=1)
    pad2Button.grid(row=1, column=1)
    pad3Button.grid(row=1, column=2)

    pad4Button.grid(row=2)
    pad5Button.grid(row=2, column=1)
    pad6Button.grid(row=2, column=2)


main_window = Tk()
main_window.resizable(False, False)
main_window.title('Beat Board')
create_layout()
main_window.mainloop()
