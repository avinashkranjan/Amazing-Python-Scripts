# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:50:06 2020

@author: quent
"""
import PyPDF2
import pyttsx3
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw() # We could make our own GUI but let's use the default one
FILE_PATH = askopenfilename() # open the dialog GUI

with open(FILE_PATH, "rb") as f:  # open the file in reading (rb) mode and call it f
    pdf = PyPDF2.PdfFileReader(f)
    #parse every page
    for page in pdf.pages:
        text = page.extractText()
        ## speaking part ####
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
