import requests
import pyfiglet
import itertools
import threading
import time
import sys

url = "https://simple-chatgpt-api.p.rapidapi.com/ask"


headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "OUR API KEY",
    "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)

    # Clear the console output
    sys.stdout.write('\r')
    sys.stdout.flush()


def ask(question):
    payload = {"question": question}
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("answer")


if __name__ == "__main__":
    print(pyfiglet.figlet_format("AI Chat BOT"))
    print("Enter the question to ask:")
    print()
    while True:
        # print("/>>  ", end="")
        question = str(input(">>  "))
        if (question == 'q'):
            print(">>  Bye! Thanks for Using...")
            break
        # loading
        done = False
        # here is the animation
        t = threading.Thread(target=animate)
        t.start()
        answer = ask(question)
        time.sleep(5)
        done = True
        t.join()
        print(">> ", answer)
        print()
