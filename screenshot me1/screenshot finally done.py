import pyautogui, time
time.sleep(5)
screenshot = pyautogui.screenshot()
screenshot.save('image1.png')
print('screenshot taken.')
