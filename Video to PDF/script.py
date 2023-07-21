from tkinter import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from fpdf import FPDF
import threading
import speech_recognition as sr
import os


# variables
video_clip = ''
audio_clip = ''

# function to get video


def get_video():
    global video_filepath, video_clip
    try:
        video_filepath.set(filedialog.askopenfilename(
            title="Select your video file"))
        video_clip = VideoFileClip(str(video_filepath.get()))
    except:
        messagebox.showerror("Error", "No video selected")


# function to convert audio to pdf
def audio_to_pdf():
    global audio_clip
    try:
        audio_clip = video_clip.audio.write_audiofile(r"my_audio.wav")
        r = sr.Recognizer()
        with sr.AudioFile("my_audio.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            write_file = open('my_text.txt', 'w')
            write_file.write(text)
            write_file.close()
            text_to_pdf('my_text.txt')
        messagebox.showinfo("Message", "Conversion Successfull")
    except:
        messagebox.showerror("Error", "Conversion not performed")

    video_filepath.set('')

    progress_bar['value'] = 0
    progress_bar.stop()

    os.remove("my_audio.wav")
    os.remove("my_text.txt")

# function to convert text to pdf


def text_to_pdf(file):
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    effective_page_width = pdf.w - 2*pdf.l_margin

    f = open(file, "r")

    for x in f:
        pdf.multi_cell(effective_page_width, 0.15, x)
        pdf.ln(0.5)

    pdf.output("../Video to PDF/my_pdf.pdf")


# function to run the script
def run():
    global progress_bar
    t1 = threading.Thread(target=progress_bar.start)
    t2 = threading.Thread(target=audio_to_pdf)
    t2.start()
    t1.start()


# GUI CODE
# Intializing main program settings
root = Tk()
root.title("Video to PDF Converter")

# Variables for file paths
video_filepath = StringVar()

# Creating UI Frame
UI_frame = Frame(root, width=500, height=500, relief="raised")
UI_frame.grid(row=0, column=0)

convert_frame = Frame(root, width=500, height=500, relief="raised")
convert_frame.grid(row=1, column=0)

# Labels and buttons
select = Label(UI_frame, text="Select Video : ", font=("Arial", 12))
select.grid(row=1, column=1, padx=5, pady=5, sticky=W)

browse = Button(UI_frame, text="Browse", command=get_video, font=("Arial", 12))
browse.grid(row=1, column=2, padx=5, pady=5)

video_selected = Label(UI_frame, text="Selected video : ",  font=("Arial", 12))
video_selected.grid(row=2, column=1, padx=5, pady=5, sticky=E)

video_path = Label(UI_frame, textvariable=video_filepath)
video_path.grid(row=2, column=2, padx=2, pady=5, sticky=W)

convert = Button(convert_frame, text="Convert",
                 command=run,  font=("Arial", 12))
convert.grid(row=3, column=1, pady=5)

progress_bar = ttk.Progressbar(
    root, orient=HORIZONTAL, mode='indeterminate', length=500)
progress_bar.grid(padx=25, pady=25)

# Calling main program
root.mainloop()
