import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
import sys
from pprint import pprint
from selenium import webdriver
import json
from win10toast import ToastNotifier
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
key='12345'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning Mr. Stark!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mr. Stark!")

    elif hour>=18 and hour<24:
        speak("Good Evening Mr. Stark")

    else:
        speak("Good Night Mr. Stark")
    
    
    speak("Jarvis at your Service. Please enter the passcode")

def takepasscode():
    r=sr.Recognizer()
    access=False
    with sr.Microphone() as source:
        print("Passcode")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Verfying...")
        passcode = r.recognize_google(audio, language='en-in')
        print(f"Mr. Stark Said:{passcode}\n")
        if passcode==key:
            access=True
            print("Entered passcode is correct")
        else:
            access=False
            print("Entered passcode is incorrect")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return access
    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..!!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Mr. Stark Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please..!!")
        speak("Say that again Please..!!")
        return "None"
    return query

'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Senderemail@gmail.com', 'Password')
    server.sendmail('Senderemail@gmail.com', to, content)
    server.close()
'''          

if __name__ == "__main__":
    wishMe()
    passcode=takepasscode()   
    while passcode:#replace True with passcode
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(f'{query}', sentences=5 )
            speak('According to Wikipedia')
            print(results)
            speak(results)


        elif 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
                
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' +text +'.com')
                wb.get(chrome_path).open(text+'.com')
            except Exception as e:
                print(e)

        
        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            print(strTime)    
            speak(f"Sir, the time is {strTime}")
            
            
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            print(date,month,year)
            speak(date)
            speak(month)
            speak(year)


        elif 'email to harry' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ReciversEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")


        elif 'quit' in query:
            shutdown = input("Please type if you wish to shutdown your computer ? (yes / no): ") 
            if shutdown == 'no': 
                exit() 
            else: 
                os.system("shutdown /s /t 1")


        elif 'what about you' in query:
            speak("In Peter David's novelization of Iron Man, J.A.R.V.I.S. is said to be an acronym for Just A Rather Very Intelligent System JARVIS is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent.")
            print("In Peter David's novelization of Iron Man, J.A.R.V.I.S. is said to be an acronym for Just A Rather Very Intelligent System.JARVIS is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent.")
        

        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        #covid-19 updates
        elif 'covid-19 update' in query:
            r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
            data = r.json()
            text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'		
            while True:
                print("Check your notifications..!!")
                speak(text)
                toast = ToastNotifier()
                toast.show_toast("Covid-19 Notification",text ,duration=20)
                sleep(60)

        #play music
        elif 'play music' in query:
            os.startfile("E:\\code\\PYTHON\\PROJECTS\\JARVIS-py-master\\fav.mp3")

        #open youtube
        elif 'youtube' in query:
            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        
        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            you(takeCommand())


        elif 'code' in query:
            codePath = "E:\\code"#ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)


        elif 'your master' in query:
            speak('Yash Verma is my master. He created me when he was in 5th semester.')
        

        elif 'your name' in query:
            speak('My name is JARVIS')

        
        elif 'thank you' in query:
            print("Glad to help You. It was the least I could do.")
            speak("Glad to help You. It was the least I could do.")


        elif 'sleep' in query:
            sys.exit()
        

        elif 'bye' in query:
            print("Bye Mr.Stark")
            speak("Bye Mr.Stark")
            break



        elif 'how is the weather' in query:

            url = 'https://api.openweathermap.org/'#Open api link here

            
            # 7e5f245b53a42f1e4416a0a2644cafcf api

            res = requests.get(url)

            data = res.json()


            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))

'''      

        elif 'turn on lights' in query:
            speak("OK,sir turning on the Lights")
            lighton()
            speak("Lights are on")
            
        elif 'turn off lights' in query:
            speak("OK,sir turning off the Lights")
            lightoff()
            speak("Lights are off")

        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()
'''
            
            


        
        
