from gtts import gTTS
from playsound import playsound

# Function to convert text to speech
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# Take input from the user
text = input("Enter your text: ")

# Specify the output filename
filename = "output.mp3"

# Convert text to speech
text_to_speech(text, filename)

# Play the generated speech
playsound(filename)