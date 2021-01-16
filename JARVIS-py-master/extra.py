def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)

    if hour>=6 and hour<12:
        speak("Good Morning Mr. Stark!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mr. Stark!")

    elif hour>=18 and hour<24:
        speak("Good Evening Mr. Stark")

    else:
        speak("Good Night Mr. Stark")

    speak("Jarvis at your Service. Please tell me how can I help You ")



def lighton():
    driver = webdriver.Chrome('C:/Users/Username/Downloads/chromedriver.exe')add the location of the chrome Drivers
    driver.get("https://Add here.000webhostapp.com/main.html")Add the webhost name
    elem1 = driver.find_element_by_id("S1off")
    elem1.click()

def lightoff():
    driver = webdriver.Chrome('C:/Users/HACKER47/Downloads/chromedriver.exe')
    driver.get("https://Add here.000webhostapp.com/main.html")Add the webhost name
    elem1 = driver.find_element_by_id("S1on")
    elem1.click()
'''  