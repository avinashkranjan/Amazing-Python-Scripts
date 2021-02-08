import os 
import time
import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import pyttsx3

def speak(text):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    randfile = str(r2)+"randomtext"+str(r1) +".mp3"
    tts = gTTS(text= text, lang='en', slow=False)
    tts.save(randfile)
     
    playsound.playsound(randfile)
    print(randfile)
    os.remove(randfile)
  
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("say anything : ")
        audio= r.listen(source)
        try:
            said = r.recognize_google(audio)
            print(said)
        except:
            print("sorry, could not recognise")
    
    return said
     
engine = pyttsx3.init()
engine.say("hello sir!, This is, Robot, Created by ,Sai Harsha , How can help you?")
#engine.setProperty('rate', 120) 
engine.runAndWait()
text = get_audio()
if "PDF" or "pdf" in text:
    engine = pyttsx3.init()
    engine.say("Yes sir y not,")
    engine.setProperty('rate', 125) 
    engine.runAndWait()
    os.system(r"slides\sample.pdf")

elif  "Google" or "google" or "GOOGLE" in text:
    engine = pyttsx3.init()
    engine.say("Yes sir y not,")
    engine.setProperty('rate', 125) 
    engine.runAndWait()
    os.system("start \"\" https://www.google.com")
