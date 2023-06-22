# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:26:25 2020

@author: Avinash Ranjan
"""

import re

print("Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = input("Enter Equation: ")

    if equation == 'quit':
        print("Goodbye, Human..!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()"{}"]', '', equation)

        try:
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)
        except Exception as e:
            print("Invalid equation. Please try again.")

while run:
    performMath()
