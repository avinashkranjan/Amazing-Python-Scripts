import pyautogui as pgui
import time

def travelScreen():
    pgui.FAILSAFE = False

    screenWidth, screenHeight = pgui.size()    # screen resolution 
    print(f"screenWidth : {screenWidth}, screenHeight : {screenHeight}")

    pgui.moveTo(2, 2)

    initial_x, initial_y = pgui.position()
    print(f"Initial x : {initial_x}, Initial y : {initial_y}")


    for x in range(initial_x, screenWidth - 2):
        for y in range(initial_y, screenHeight - 2):
            print(pgui.position())
            pgui.moveTo(x,y)

if __name__ == "__main__":
    travelScreen()