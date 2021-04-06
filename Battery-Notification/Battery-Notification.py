import psutil
from plyer import notification
import time
#From psutil we import sensors battery class which gives us battery percentage
while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    notification.notify(
        title = "Battery Percentage",
        message = str(percent) + "% Battery Remaining",
        timeout = 5
        )
     #After every 60 minutes it will show the battery percentage via a notification   
    time.sleep(60)
    continue
