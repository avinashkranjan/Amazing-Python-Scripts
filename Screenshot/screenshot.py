import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'E:/Python-Programs/PythonProjects/Screenshot/ScreenshotsData/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()
