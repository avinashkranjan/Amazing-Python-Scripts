import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import cv2


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# use [1]->female voice and [0]-> male voice
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening.....(speak now)")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "google" in command:
                command = command.replace("google", '')
                print(command)
    except:
        print("Ooops something went wrong!")

        pass
    return command


def run_mini_google_assistant():

    command = take_command()
    print(command)

    if "play" in command:
        song = command.replace("play", "")
        talk("playing the song" + song)
        print(song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M%p")
        print(time)
        talk("Current time is" + time)
    elif "joke" in command:
        talk("Here is the joke")
        talk(pyjokes.get_joke())
        talk("   heeheehehe quite funny!  ")
    elif 'date' in command:
        date = datetime.date.today()
        print(date)
        talk("Today is")
        talk(date)
    elif 'how are you' in command:
        talk('I am good. Nice to see you here!')
    elif "capture" or "camera" in command:
        talk("Ok I'll do it for you!")
        talk("Remenber, You can use s button to quit")
        vid = cv2.VideoCapture(0)

        while (True):

            # Capture the photo/video frame by frame
            ret, frame = vid.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)

            if "photo" in command:
                if cv2.waitKey(0) & 0xFF == ord('s'):  # used 's' as quitting button
                    #talk("You can use s button to quit")
                    break
            elif "video" in command:
                if cv2.waitKey(1) & 0xFF == ord('s'):  # used 's' as quitting button
                    #talk("You can use s button to quit")

                    break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    else:
        talk("Sorry i am not getting you! Can you please repeat!")


talk("Hello my friend, i am your personal mini google assistant.")
talk("And i can help you to play song, tell time, tell date, tell joke and i can also capture photo and video for you")
talk("Now please tell me how can i help you!")
while True:
    run_mini_google_assistant()
    #talk("Nice to see you here, I belive that you enjoyed!")
