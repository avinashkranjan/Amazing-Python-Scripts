from selenium import webdriver
from PIL import Image
import pytesseract
import io
import numpy as np
import cv2 as cv
import time
import tkinter   
from tkinter import ttk
from webdriver_manager.chrome import ChromeDriverManager


def click():
    global inputpnrnumber
    inputpnrnumber = str(name.get()) 
    if (inputpnrnumber.isnumeric()) and ( len(inputpnrnumber) == 10 ) :
        window.destroy()


def GUI() :
    window.title("PNR STATUS")
    lbl = ttk.Label(window, text = "                         ")
    lbl.grid(column = 0, row = 0) 
    lbl = ttk.Label(window, text = "    Enter PNR Number:    ")
    lbl.grid(column = 0, row = 1)
    nameEntered = ttk.Entry(window, width = 12, textvariable = name)
    nameEntered.grid(column = 1, row = 1)
    lbl = ttk.Label(window, text = "            ")
    lbl.grid(column = 2, row = 1)
    lbl = ttk.Label(window, text = "                        ")
    lbl.grid(column = 1, row = 2) 
    button = ttk.Button(window, text = "Submit", command = click)
    button.grid(column = 1, row = 3)
    lbl = ttk.Label(window, text = "                         ")
    lbl.grid(column = 1, row = 4) 
    window.mainloop()

window = tkinter.Tk()
name = tkinter.StringVar()    
url="http://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html?locale=en"

GUI()

#google = input(r"Enter google executable path");
tess = input(r"Enter tesseract path: ");

browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())   
browser.get(url)
pnrnumber = browser.find_element_by_id('inputPnrNo')
pnrnumber.send_keys(inputpnrnumber)
close = browser.find_element_by_id('corover-close-btn')
close.click()
submit = browser.find_element_by_id('modal1')
submit.click()
captchascreenshot = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div/div/div/div[2]/div[2]/div/div[2]")
time.sleep(2)  
screenshotimagebinary = captchascreenshot.screenshot_as_png
img_array = np.array(bytearray(screenshotimagebinary), dtype=np.uint8)
img = cv.imdecode(img_array, 0)
(thresh, blackAndWhiteImage) = cv.threshold(img, 120,255, cv.THRESH_BINARY)
pytesseract.pytesseract.tesseract_cmd = tess
prob = pytesseract.image_to_string(blackAndWhiteImage) 
prob = prob.replace('=', ' ')
prob = prob.replace('?', ' ')
add = prob.find('+')
subtract = prob.find('-')
if add != -1 :
    k=1
    prob = prob.replace('+', ' ')
if subtract != -1 :
    k=2
    prob = prob.replace('-', ' ')
j = 0
while j < len(prob):
    q = prob[j]
    if not(q.isdigit()):
        prob = prob.replace(prob[j], ' ')
    j+=1
    
i = prob.split(" ", 1)
print(prob)
num1=int(i[0])
num2=int(i[1])
if k == 1 :
    sol=num1+num2
if k == 2 :
    sol=num1-num2
print(str(sol))
ans = browser.find_element_by_id('inputCaptcha')
ans.send_keys(str(sol))
time.sleep(1)  
submit1 = browser.find_element_by_id('submitPnrNo')
submit1.click()
time.sleep(3)

screenshot = browser.find_element_by_xpath("//html/body/div[2]/div[2]/div[2]")
screenshotimagebin = screenshot.screenshot_as_png
imgarray = np.array(bytearray(screenshotimagebin), dtype=np.uint8)
img1 = cv.imdecode(imgarray, cv.IMREAD_COLOR)
cv.imshow("PNR STATUS",img1)
cv.imwrite("PNRSTATUS.png", img1)

