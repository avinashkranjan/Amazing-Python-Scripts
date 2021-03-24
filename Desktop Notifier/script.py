import time
from plyer import notification

    
heading = input("Enter the title: ")

description = input("Enter the message: ")
timer = int(input("Enter the timeer: "))
notification.notify(
    title = heading,
    message= description ,
    app_icon = None,
    # displaying time
    timeout=2 ,
    toast=False)

 # waiting time
time.sleep(7)

