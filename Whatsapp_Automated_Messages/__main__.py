import pyautogui as pt 
import time
import pyperclip
import random 

time.sleep(4)

position1 = pt.locateOnScreen("Whatsapp_Automated_Messsages/smilie_paperclip.png", confidence=.6)
x= position1[0]
y= position1[1]


def get_message():             # it will help us to fetch the messages
    global x, y
    position = pt.locateOnScreen("./Whatsapp_Automated_Messsages/smilie_paperclip.png", confidence=.6)
    x= position1[0]
    y= position1[1]
    pt.moveTo(x,y)   # add duration for mac: pt.moveTO(x,y, duration=.05)
    pt.moveTo(x+70, y-40)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRe(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_message)
    return whatsapp_message

def post_response(message):               # to post our desire response

    global x, y 
    position = pt.locateOnScreen("./Whatsapp_Automated_Messsages/smilie_paperclip.png", confidence=.6)
    x= position1[0]
    y= position1[1]
    pt.moveTo(x+200, y+20)
    pt.click()
    pt.typewrite(message, interval= .01)

    pt.typewrite("\n", interval=0.01)

def process_responses(message):        # to check what is the response sutaible for the message received
    random_no=random.randrange(5)

    if "Thank You" in str(message).lower():
        return "You are always welcome!"

    elif "Happy Birthday" in str(message).lower():
        return "Thank you"

    elif "Good Morning" in str(message).lower():
        return "Have nice day ahead"

    elif "Good Night" in str(message).lower():
        return "Good Night! Sleep Well"
    
    elif "Sorry" in str(message).lower():
        return "It's Okay"

    elif "Thanks" in str(message).lower():
        return "Mention Not"
    
    else:
        if random_no==0:
            return "Talk to you later"

        elif random_no==1:
            return "Will catch you in sometime"

        else:
            return "A bit busy!"

def new_message_check():       # to keep checking if new message is received
    pt.moveTo(x+50, y-35)

    while True:
        try:
            position= pt.locateOnScreen("./Whatsapp_Automated_Messsages/green_mark.png", confidence=.6)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                time.sleep(2)

        except(Exception):
            print("No new messages")

        if pt.pixelMatchesColor(int(x+50),int(y-35),(255,255,255), tolerance=10):
            print("is white")
            processed_message= process_responses(get_message())
            post_response(processed_message)

        else:
            print("No new messages yet...")

        time.sleep(5)

      

new_message_check()

    
    
