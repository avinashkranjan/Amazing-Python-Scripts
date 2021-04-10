import psutil
from plyer import notification
import time
#From psutil we import sensors battery class which gives us battery percentage
threshold = int(input('Enter the threshold: '))
while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    time.sleep(60*2)
    battery = psutil.sensors_battery()
    cur_per = battery.percent
    change = cur_per - percent
    diff = abs(change)
    #We calculate the change in the battery and show notification if battery level increases or decreases
    if(diff >= threshold):
        notification.notify(
            title = "Battery Percentage",
            message = str(percent) + "% Battery Remaining",
            timeout = 5
        )   
    continue
