import pyttsx3

data = input("Enter Text You Want To Covert: \n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()

