# Random Name Picker Using Python

# The Python Script should:
# Generate random names that will be included in the unique name.
# Allow the user to enter name of their choice
# importing Libraries
from random import randint
# Welcome Statement
print("\nWelcome to the Random Name Picker by Ruchita!")
# input by the user
input("Press a key to continue......")
# Input how many names user want to use
name_amount = int(input("\nInput how many names u want to use: "))
names = []
for x in range(name_amount):
    k = input("Enter name : \n")
    names.append(k)
# Random name picker
random_number = randint(0, len(names))
name_number = (random_number - 1)
random_name = names[name_number]
print("\nThe number of the name is : " + str(name_number) + "!!")
print("\nRandomly selected name is: " + random_name + "!!" + " Congrats!")
input("Press a key to continue......")
