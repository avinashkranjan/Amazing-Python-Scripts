from tkinter import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import threading

# Variables for video and audio files
video_file = ''
audio_file = ''


def get_video_file():
    """
    Function that gets the video file that needs to be converted
    """
    global video_filepath, video_file
    video_filepath.set(filedialog.askopenfilename(title="Select your video file", filetypes=[
        ('MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)',
         '*.mp4 *.m4a *.m4v *.f4v *.f4a *.m4b *.m4r *.f4b *.mov'),
        ('3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)', '*.3gp *.3gp2 *.3g2 *.3gpp *.3gpp2'),
        ('OGG (ogg, oga, ogv, ogx)', '*.ogg *.oga *.ogv *.ogx'),
        ('WMV (wmv, wma)', '*.wmv *.wma'),
        ('FLV', '*.flv'), ('AVI', '*.avi'), ('MPEG-1 (mpg, mp2, mpeg, mpe, mpv )',
                                             '*.mpg *.mp2 *.mpeg *.mpe *.mpv'),
        ('MPEG-2', '*.mpg *.mpeg *.m2v')]))
    video_file = VideoFileClip(str(video_filepath.get()))


def save_audio_file():
    """
    Function that converts video file into audio file in a path that the user chooses
    """
    global audio_filepath, audio_file, progress_bar
    audio_filepath.set(filedialog.asksaveasfilename(defaultextension='.mp3',
                                                    title="Select your audio file directory", filetypes=[
                                                        ('MP3 File', '*.mp3'), ('Wave File', '*.wav')]))
    try:
        audio_file = video_file.audio
        audio_file.write_audiofile(str(audio_filepath.get()))
        video_file.close()
        audio_file.close()
        messagebox.showinfo(message="File converted successfully")
    except:
        messagebox.showerror(
            message="File could not be converted", title="File Error")
    # Resetting the video and audio paths
    video_filepath.set('')
    audio_filepath.set('')
    # Resetting the progressbar after function execution
    progress_bar['value'] = 0
    progress_bar.stop()


def run_program():
    """
    Function that runs the process of conversion and loading bar concurrently
    """
    global progress_bar
    t1 = threading.Thread(target=progress_bar.start)
    t2 = threading.Thread(target=save_audio_file)
    t2.start()
    t1.start()


# Intializing main program settings
main_prog = Tk()
main_prog.title("Video to Audio Converter")
main_prog.maxsize(800, 400)
main_prog.minsize(500, 200)
main_prog.config(bg="ivory")


# Variables for file paths
video_filepath = StringVar()
audio_filepath = StringVar()

# Creating UI Frame
UI_frame = Frame(main_prog, width=500, height=500, bg="ivory")
UI_frame.grid(row=0, column=0)

# Labels and buttons of the program
Label(UI_frame, text="Choose your video file", bg="ivory").grid(
    row=1, column=1, padx=5, pady=5, sticky=W)
Button(UI_frame, text="Browse", command=get_video_file,
       bg="grey").grid(row=1, column=2, padx=5, pady=5)
Button(UI_frame, text="Convert", command=run_program,
       bg="green").grid(row=2, column=2, padx=5, pady=5)
Label(UI_frame, textvariable=video_filepath, bg="ivory").grid(
    row=1, column=3, padx=5, pady=5, sticky=W)


progress_bar = ttk.Progressbar(
    main_prog, orient=HORIZONTAL, mode='indeterminate', length=500)
progress_bar.grid(padx=25, pady=25)

# Calling main program
main_prog.mainloop()
