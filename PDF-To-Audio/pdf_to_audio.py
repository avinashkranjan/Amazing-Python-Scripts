# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:50:06 2020

@author: quent
"""
import PyPDF2
import pyttsx3
from gtts import gTTS  # pip install gTTS
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # We could make our own GUI but let's use the default one
FILE_PATH = askopenfilename()  # open the dialog GUI

with open(FILE_PATH,
          "rb") as f:  # open the file in reading (rb) mode and call it f
    pdf = PyPDF2.PdfFileReader(f)
    txt_file = ' '  # str variable
    # parse every page
    for page in pdf.pages:
        text = page.extractText()
        txt_file += text  # stores text into txt_file variable and convert it into str form as gtts library only saves text file into mp3
        ## speaking part ####
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
audio_file = gTTS(text=txt_file, lang='en')  # stores into variable
# saves into mp3 format with the same name of pdf in the same directory where pdf is
audio_file.save(FILE_PATH.split('.')[0] + ".mp3")
