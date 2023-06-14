import speech_recognition as sr

def convert_audio_to_text():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Open the microphone and start recording
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)  # Record audio from the microphone

    try:
        # Use the recognizer to convert audio to text
        text = r.recognize_google(audio)  # Convert audio to text using Google Speech Recognition service
        return text
    except sr.UnknownValueError:
        print("Unable to recognize speech.")  # Handle the case when speech cannot be recognized
    except sr.RequestError as e:
        print("Error: {0}".format(e))  # Handle any errors that occur during speech recognition

# Example usage
audio_text = convert_audio_to_text()  # Call the function to convert audio to text
if audio_text:
    print("You said:", audio_text)  # Print the converted text

# Manipulate the text for further operations
if audio_text:
    # Convert the text to lowercase
    lowercase_text = audio_text.lower()
    print("Lowercase text:", lowercase_text)

    # Split the text into words
    words = lowercase_text.split()
    print("Words:", words)

    # Perform other operations on the text as needed
    
