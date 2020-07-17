import time
import pyautogui                

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'E:/Python-Programs/PythonProjects/Screenshot/ScreenshotsData/{}.png'.format(name)       # To name the file
    time.sleep(5)           #  Time Wait Before Taking Screenshot 
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()
