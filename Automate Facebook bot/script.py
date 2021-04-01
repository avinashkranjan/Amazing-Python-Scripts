import pyautogui
import time

number = int(input("Enter number of groups: "))
groupid = []
print("Enter group ids: ")
for i in range(number):
    ele = input()
    groupid.append(ele) 

time.sleep(5)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')

pyautogui.keyUp('ctrl')

for i in range(number):
    link = 'https://facebook.com/groups/'+groupid[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    print("Waiting for few seconds .......")
    time.sleep(45)
    pyautogui.typewrite('p')
    time.sleep(2)
    pyautogui.typewrite('Hello! I am facebook bot')
    time.sleep(4)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    pyautogui.write(['f6'])
    time.sleep(1)

