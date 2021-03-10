import sys
from moviepy.editor import VideoFileClip

def toMp3(vidName):
    """Returns the name of the audio file with *.mp3 extention."""
    audio = vidName + ".mp3"
    return audio

def toWav(vidName):
    """Returns the name of the audio file with *.wav extension."""
    audio = vidName + ".wav"
    return audio

if __name__ == "__main__":
    """Accepts user input, handles exception and bad input, converts *.mp4 to audio file and write it in the folder."""
    vid = input("\nEnter the name of the video along with the \".mp4\" extension : ")

    try: vidName, vidFormat = vid[:vid.index(".")], vid[vid.index(".")+1:]
    except:
        print("\nFaulty Input. Check Again!\n")
        sys.exit(0)
    
    if vid.count(".") > 1:
        print("\nFaulty Input. Check Again!\n")
        sys.exit(0)
    
    print(f"Video Name : {vidName}\nVideo Format : {vidFormat}")

    if vidFormat != "mp4" and vidFormat != "MP4":
        print("\nPlease input a video with \".mp4\" format.\n")
        sys.exit(0)

    try: videoClip = VideoFileClip(vid)
    except:
        print("\nVideo could not be found in the folder.\nKindly check your folder and try again.\n")
        sys.exit(0)

    audformat = input("\nWhich format would you like your audio file to be in?\n(1)   *.mp3\n(2)   *.wav\nChoose 1 or 2 : ")
    audioClip = videoClip.audio

    if audformat == "1": audio = toMp3(vidName)
    elif audformat == "2": audio = toWav(vidName)
    else:
        print("Bad Input!\nInput did not comply with the choices.")
        sys.exit(0)

    audioClip.write_audiofile(audio)

    videoClip.close()
    audioClip.close()

    print("\nAudio File Generation Successful!\n")