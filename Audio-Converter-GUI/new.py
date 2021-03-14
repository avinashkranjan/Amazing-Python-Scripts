import tkinter as tk
import time
import sys
from moviepy.editor import VideoFileClip

global count

def storeText():
    global e
    vid = e.get()

    global vidName , vidFormat , videoClip
    try: vidName, vidFormat = vid[:vid.index(".")], vid[vid.index(".")+1:]
    except:
        label2 = tk.Label(root,text = "Faulty Input. Check Again!")
        label2.pack()

    if vid.count(".") > 1:
        label3 = tk.Label(root,text = "Faulty Input. Check Again!")
        label3.pack()
        
    
    label4 = tk.Label(root,text = f"Video Name : {vidName}\nVideo Format : {vidFormat}\n")
    label4.pack()

    try: videoClip = VideoFileClip(vid)
    except:
        label5 = tk.Label(root,text = "Video could not be found in the folder.\nKindly check your folder and try again!")
        label5.pack()

    labelChoice = tk.Label(root, text = "Which format would you like your audio file to be in?\n(1)   *.mp3\n(2)   *.wav\nChoose 1 or 2 : ")
    labelChoice.pack(pady=20)


    button1 = tk.Button(root,text = "1",command = first )
    button2 = tk.Button(root,text = "2",command = second )

    button1.pack(pady=20)
    button2.pack(pady=20)

    
def first():
    global vidName , vidFormat , videoClip 
    try:
        audioClip = videoClip.audio  
        audio = toMp3(vidName)
        audioClip.write_audiofile(audio)
        
    except Exception as e:
        videoClip.close()
        audioClip.close()
        

def second():
    global vidName , vidFormat , videoClip 

    try:
        audioClip = videoClip.audio
        audio = toWav(vidName)
        audioClip.write_audiofile(audio)

    except Exception as e:
        videoClip.close()
        audioClip.close()


def toMp3(vidName):
    """Returns the name of the audio file with *.mp3 extention."""
    audio = vidName + ".mp3"
    ll = tk.Label(root,text = "Audio File Generation Successful!")
    ll.pack(pady = 10)

    time.sleep(3)
    exit_button = tk.Button(root, text="Exit", command=root.destroy) 
    exit_button.pack() 

    return audio

def toWav(vidName):
    """Returns the name of the audio file with *.wav extension."""
    audio = vidName + ".wav"
    ll = tk.Label(root,text = "Audio File Generation Successful!")
    ll.pack(pady = 10)

    time.sleep(3)
    exit_button = tk.Button(root, text="Exit", command=root.destroy) 
    exit_button.pack() 
    
    return audio



root = tk.Tk()


root.title("Video to Audio Converter")

root.geometry("800x550")


w = tk.Label(root, text ='Video To Audio Converter', font = "50")    
w.pack(pady = 20) 


label = tk.Label(root,text = "Enter the name of the video along with the file extension.\nEg. \"abc.flv\" : ")
label.pack(pady=20)

e = tk.Entry(root)
e.pack()
e.focus_set()


button = tk.Button(root,text = "Check",command = storeText)
button.pack(pady=20)

root.mainloop()