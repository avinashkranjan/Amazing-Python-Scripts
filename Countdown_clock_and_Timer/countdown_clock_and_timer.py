# import modules like 'os' and 'time'
import os
import time

os.system('clear')

# using ctime() to show present time
times = time.ctime()
print("\nCurrent Time: ", times)

print(
    "\n     Welcome to CountdownTimer!\n\n     Let's set up the countdown timer...\n"
)

# User input for the timer
hours = int(input("     How many hours? "))
minutes = int(input("     How many minutes? "))
seconds = int(input("     How many seconds? "))

# To display message when the given value is not a number
if hours or minutes or seconds == "":
    print("\n Invalid entry. You must enter a number.")

# Conversion of hours amd minutes into seconds
hrsToSec = (hours * 60) * 60
mnsToSec = (minutes * 60)
seconds = seconds

seconds = hrsToSec + mnsToSec + seconds
print("\n Timer has been set for " + str(seconds) + " seconds.")

# Loop for displaying the timer

for i in range(seconds, -1, -1):
    displayHours = int(seconds / 3600)
    displayMinutes = int(seconds / 60)
    if displayMinutes >= 60:
        displayMinutes = displayMinutes - (displayHours * 60)
    else:
        displayMinutes = displayMinutes
    displaySeconds = int(seconds % 60)
    print("\n     Your time remaining is: {}:{}:{}".format(
        str(displayHours).zfill(2),
        str(displayMinutes).zfill(2),
        str(displaySeconds).zfill(2)))
    seconds -= 1
    time.sleep(1)  # delays in the excution of a program for 1 second

print("\n Time is over.")
