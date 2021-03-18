import pyautogui as pt 
import time

while True:
    posXY=pt.position()
    print(posXY,pt.pixel(posXY[0],posXY[1]))
    time.sleep(3)

    if posXY[0]==0:
        break

