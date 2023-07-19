import pyjokes
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+-20)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def joke():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    joke()
