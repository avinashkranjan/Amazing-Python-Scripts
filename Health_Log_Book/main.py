# It is a health management system
# Consists of food and exercise log table
# Has the fascility both to enter a log and to retrieve the log
# Helps the user to inspect his/her health

# importing the modules
import datetime

# creating a function to return date and time
def getdate():
    return datetime.datetime.now()

# defining a function to take the inputs from the user and store the input data in a text file    
def take():
        x = int(input("enter 1 for exercise and 2 for food"))
        if x==1:
            val = input("enter each exersise separated with commas\n")
            with open("user-exercise.txt","a") as f:
                f.write(str([str(getdate())]) + ":- " + val + "\n")
            print("successfully written")
        elif x==2:
            val = input("enter each food separated with commas\n")
            with open("user-food.txt", "a") as f:
                f.write(str([str(getdate())]) + ":- " + val + "\n")
            print("successfully written")

# defining a function to retrieve the data from the text file
def retrieve():
        x = int(input("enter 1 for exercise and 2 for food"))
        if x == 1:
            with open("user-exercise.txt") as f:
               for i in f:
                   print(i,end=" ")
        elif x == 2:
            with open("user-food.txt") as f:
                for i in f:
                    print(i, end=" ")

# Testing code
print("Health log book: ")
a = int(input("press 1 for log and 2 for retrieve"))

if a==1:
    take()
else:
    retrieve()
