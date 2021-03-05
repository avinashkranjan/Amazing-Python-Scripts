# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:26:25 2020

@author: Avinash Ranjan
"""
#Import regex 
import re

print("Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

# Generate a function to perform basic Calculations
def performMath():
    global run
    global previous

    #Initialize equation
    equation = ""

    # ask user for an input equation and print result
    if previous == 0:
        equation = input("Enter Your Equation: ")
        
    else:
       equation = input(f"your Result : {str(previous)} , Enter Another Equation or quit : ").lower()

    # If user input is 'quit'
    if equation == 'quit' or equation == '' :
        print("GoodBye, See you later!")
        #Exit code by setting run as false
        run = False

    else:
        # strip special characters and alphabets
        equation = re.sub('[a-zA-Z,:()"{}"]', '', equation)

        #perform operation
        if previous == 0:
            previous = eval(equation)
            
        else:
            previous = eval(str(equation) + equation)

# While run is True, perform math operation
while run:
    performMath()
