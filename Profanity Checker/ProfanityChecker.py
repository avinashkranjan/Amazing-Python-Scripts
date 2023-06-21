import speech_recognition as sr
import requests
import nltk
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import filedialog

nltk.download('wordnet')

nltk.download('punkt')
nltk.download('stopwords')

# Initialize the recognizer
r = sr.Recognizer()

# Ask the user whether to record from the microphone or select a file
root = tk.Tk()
root.withdraw()
mode = input("Enter 'mic' to record from microphone or 'file' to select a file: ")

if mode == 'mic':
    # Record audio from the user
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Use Google Speech Recognition to convert audio to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

elif mode == 'file':
    # Select a file using a dialog box
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)

    # Convert audio file to audio data
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)

    # Use Google Speech Recognition to convert audio to text
    try:
        text = r.recognize_google(audio)
        print("Transcription: " + text)
        

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

else:
    print("Invalid mode selected.")

    # Preprocess the text
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
tokens = word_tokenize(text)
filtered_tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens if not w.lower() in stop_words]
filtered_text = ' '.join(filtered_tokens)

# Check for profanity in the text using the API
response = requests.get("https://www.purgomalum.com/service/json?text=" + filtered_text)
result = response.json()

if result['result'] == filtered_text:
    print("No profanity detected!")
else:
    print("Profanity detected!")
    print("Censored text: " + result['result'])

# Analyze sentiment of the text using VADER
analyzer = SentimentIntensityAnalyzer()
sentiment_scores = analyzer.polarity_scores(text)

# Print sentiment scores
print("\nSentiment Scores:")
for key, value in sentiment_scores.items():
    print(key, ': ', value)

# Print sentiment label based on compound score
sentiment_label = ''
if sentiment_scores['compound'] > 0.5:
    sentiment_label = 'Very Positive'
elif sentiment_scores['compound'] > 0:
    sentiment_label = 'Positive'
elif sentiment_scores['compound'] == 0:
    sentiment_label = 'Neutral'
elif sentiment_scores['compound'] < -0.5:
    sentiment_label = 'Very Negative'
else:
    sentiment_label = 'Negative'

print("\nSentiment Label: " + sentiment_label)

# Write input and output to CSV file
with open('profanitycheckeroutput.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    #name the columns
    writer.writerow(['Input Text', 'Filtered Text', 'Positive Score', 'Negative Score', 'Neutral Score', 'Compound Score', 'Sentiment Label'])
    #write the data

    
    writer.writerow([text, filtered_text, sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound'], sentiment_label])

