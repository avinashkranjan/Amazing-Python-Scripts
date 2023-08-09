import speech_recognition as sr
import webbrowser


def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...\n")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"\nCommand: {command}\n")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"\nError occurred while requesting results: {e}\n")
        return None


def openWebsite(website):
    website = website.replace("Open", "")
    website = website.replace(" ", "")
    url = f"https://www.{website}.com"
    webbrowser.open(url)


def displayInstructions():
    print('''\n\n1. Say "Open ${Website Name}" to open the Website.
2. Say "exit" to close the program.\n
''')


if __name__ == "__main__":
    displayInstructions()
    while True:
        command = takeCommand()

        if command == "exit":
            print("\nExiting...\n")
            print("Thanks for using this program !\n")
            break

        elif command:
            openWebsite(command)
