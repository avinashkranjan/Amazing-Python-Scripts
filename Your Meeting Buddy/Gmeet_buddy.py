#Importing Required modules and Libraries 

from selenium import webdriver
import schedule,time
import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

#joining Credentials

username = str(input('Your Username:' ))   # asking for mail id
password = str(input('Your Password:' ))   #asking for password

#Providing camera and microphone access to the meeting

opt=Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

# Passing the argument "1" to allow and "2" to block

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
    "profile.default_content_setting_values.notifications": 1 
      })
browser =webdriver.Chrome(chrome_options=opt,executable_path="C:\\Users\\path where your chrome driver is saved")   #Enter the path of your chrome driver
browser.maximize_window() 
action=ActionChains(browser)

#Function for entering into meeting as per the google meet interface
def get_into():
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Enter')

    
#Finding the scheduled meeting on the google calender.
def join_classes():
    
    browser.get("https://calendar.google.com/")
    browser.find_element_by_name("identifier").send_keys(username)
    browser.find_element_by_class_name("VfPpkd-RLmnJb").click() 

    browser.implicitly_wait(20)
    browser.find_element_by_name("password").send_keys(password)
    time.sleep(1)
    browser.implicitly_wait(40)  
    browser.find_element_by_class_name("VfPpkd-RLmnJb").click()

    browser.implicitly_wait(15)
    cursor_location=browser.find_element_by_class_name('h11RHc').location  
    x=cursor_location['x']
    y=cursor_location['y']
    action.move_by_offset(x+20,y).click().perform()
    browser.find_element_by_class_name("w1OTme").click()
#Entering Google meet
    
    time.sleep(30)
    
    keyboard.press_and_release('ctrl+e')
    keyboard.press_and_release('ctrl+d')
    print("Camera And microphone turned off")
    browser.implicitly_wait(10)
    print("About to join the class")
    get_into()
    keyboard.press_and_release('Enter')
    print("Slid into the meeting successfully")
    time.sleep(5)
    keyboard.press_and_release('Win+alt+r')
    print("meeting Recording Started")
    
join_classes()

#schedule according to your time table and quit the browser according to the time of completion of your class
# schedule.every().day.at("09:00").do(join_classes)
    
#while True:
    #schedule.run_pending()
    #time.sleep(1)
