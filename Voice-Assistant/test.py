import os
import time
import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import pyttsx3
import datetime
import time
import webbrowser
from ecapture import ecapture as ec


def speak(text):
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)
    randfile = str(r2) + "randomtext" + str(r1) + ".mp3"
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(randfile)

    playsound.playsound(randfile)
    print(randfile)
    os.remove(randfile)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold()
        print("say anything : ")
        audio = r.listen(source)
        try:
            said = r.recognize_google(audio)
            print(said)
        except:
            print("sorry, could not recognise")
    return said


engine = pyttsx3.init()
engine.say(
    "hello sir!, This is, Robot, Created by ,Sai Harsha , How can help you?")
#engine.setProperty('rate', 120)
engine.runAndWait()
text = get_audio()
if "PPT" or "ppt" or "intro" or "INTRO" in text:
    engine = pyttsx3.init()
    engine.say("Yes sir y not,")
    engine.setProperty('rate', 125)
    engine.runAndWait()
    os.system(r"d:\image.png")

elif "Google" or "google" or "GOOGLE" in text:
    engine = pyttsx3.init()
    engine.say("Yes sir y not,")
    engine.setProperty('rate', 125)
    engine.runAndWait()
    os.system("start \"\" https://www.google.com")

elif 'news' in text:
    engine = pyttsx3.init()
    news = webbrowser.open_new_tab(
        "https://timesofindia.indiatimes.com/home/headlines")
    engine.say('Here are some headlines from the Times of India,Happy reading')
    time.sleep(6)

elif 'search' in text:
    engine = pyttsx3.init()
    text = text.replace("search", "")
    webbrowser.open_new_tab(text)
    time.sleep(5)

elif 'time' in text:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    engine = pyttsx3.init()
    engine.say(f"the time is {strTime}")

elif 'open gmail' in text:
    webbrowser.open_new_tab("gmail.com")
    engine = pyttsx3.init()
    engine.say("Google Mail open now")
    time.sleep(5)

elif 'open youtube' in text:
    webbrowser.open_new_tab("https://www.youtube.com")
    engine = pyttsx3.init()
    engine.say("youtube is open now")
    time.sleep(5)

elif "camera" in text or "take a photo" in text:
    ec.capture(0, "robo camera", "img.jpg")
    engine = pyttsx3.init()
    engine.say("ok")
