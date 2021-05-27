import os
import pyttsx3
import speech_recognition as sr
import tkinter.messagebox as tmessage
import wolframalpha

from os.path import exists

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wolfprimeaplahe_app = input('Enter the API Token')


def audio(audio):
    engine.say(audio)
    engine.runAndWait()


def welcomeInst():
    print('Welcome to Calculator :)')
    audio('Welcome to Calculator :)')
    print('If you want calculate something please tell calcualte and then your expression')
    audio('If you want calculate something please tell calcualte and then your expression')
    print('For example CALCULATE 7 PLUS 8 or CALCULATE sin30 plus cot20')
    audio('For example CALCULATE 7 PLUS 8 or CALCULATE sin30 plus cot20')


def _takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio("Listning...")
        r.pause_threshold = 2
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        audio("Recognizing...")
        query = r.recognize_google(audio, language='en-In')
        print(query)

    except Exception as e:
        tmessage.showinfo('Error', f'{e}')
        print("Didn't understand you...\nCan you repeat?...")
        return "NONE"

    return query


def _calculate():
    client = wolframalpha.Client(wolfprimeaplahe_app)
    indx = spech.lower().split().index('calculate')
    query = spech.split()[indx + 1:]
    res = client.query(''.join(query))
    answerr = next(res.results).text
    space = '\n'
    ourQuery = ''.join(query)
    Question = 'Your Query was :- '
    Answer = 'Your answer was :- '
    finalAnswer = Question + str(ourQuery) + \
        space + Answer + str(answerr) + space

    if exists('./Voice Calculator/maths.txt'):
        with open('./Voice Calculator/maths.txt', 'a', encoding='utf-8') as mth:
            mth.write(finalAnswer)
            mth.close()
    else:
        history = open('./Voice Calculator/maths.txt', 'w', encoding='utf-8')
        history.write(finalAnswer)
        history.close()
    print("The answer is " + answerr)
    audio("the answer is %s" % answerr)


welcomeInst()

while True:

    spech = _takeCommand().lower()

    if 'calculate' in spech:
        _calculate()

    elif 'clear' in spech:

        if exists('./Voice Calculator/maths.txt'):
            with open('./Voice Calculator/maths.txt', 'r+') as file:
                file.truncate(0)
                file.close()
                print('done')

        else:
            tmessage.showinfo('Error', 'No file exists with this name')

    elif 'history' in spech:
        os.system('./Voice Calculator/maths.txt')

    elif 'quit' in spech or 'exit' in spech:
        quit()

    else:
        tmessage.showinfo('Opps', "Didn't understand")
