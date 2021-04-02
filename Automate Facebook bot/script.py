import pyautogui
import time
import webbrowser
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass

usr=input('Enter Email Id:') 
pwd= getpass('Enter Password:') 
num = str (input ("Enter comma separated integers: "))
lists = num.split (",")
groupid = []
for i in lists:
	groupid.append(i)

message=input("Enter your message: ")
  
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')

  
username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

  
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

  
login_box = driver.find_element_by_id('u_0_d')
login_box.submit()


time.sleep(5)

for i in range(len(groupid)):
    link = 'https://facebook.com/groups/'+groupid[i]
    webbrowser.get('chrome').open_new(link)
    print("Waiting for few seconds .......")
    time.sleep(45)
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite("Create a public post")
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite(message)
    pyautogui.click(677,520)

    time.sleep(10)
