from ctypes.wintypes import PINT
from math import gamma
from pickle import TRUE
import random
from tkinter.tix import Tree


def game(comp,mine):
    if(comp==mine):
        return None
    if(comp=='snake' and mine=='gun'):
        return True
    elif(comp=='water' and mine=='snake'):
        return True
    elif(comp=='gun' and mine=='water'):
        return True
    else:
        return False

# Here is the main code started... #

choice=('snake','water','gun')
# choice is tuple and it will not change in future
comp=random.randint(0,2)
comp=choice[comp]
# choosing one comp if user pick the value like
# 0-snake
# 1-water
# 2-gun
# 3-invalid input
mine=input('Your input:')
if(mine=='snake' or mine=='gun' or mine=='water'):
    WinTheGame=game(comp,mine)
else:
    WinTheGame=-1
print(f"You choose {mine} and the computer choose {comp}")
if WinTheGame==-1:
    print('Invalid input.')
elif WinTheGame is None:
    print('Match is drawn.')
elif WinTheGame:
    print("You Won.")
else:
    print("You Lose.")
