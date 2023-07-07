import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(30)

# Use k=1 for infinite spamming
# k=1
# while k==1:
# Else put a value in for loop for defined number of messages
for i in range(50):
    pyautogui.typewrite("Your message in")
    pyautogui.press("enter")
