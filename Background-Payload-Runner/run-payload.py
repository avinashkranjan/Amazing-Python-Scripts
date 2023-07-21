import time
import background
import os

# select which command line you want to run the payload on
# commandline="cmd /c "
commandline = "powershell "

time_delay = 0  # in seconds

# CUSTOM PAYLOAD
# rickroll payload
payload = "Start-process chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ"


# other payloads (example)
# payload="shutdown"
# --shuts down the machine without any confirmation

# payload="shutdown -force -restart"
# --restarts the machine without any confirmation
# payload="netsh wlan disconnect"
# --disconnects the wifi of the machine

# THESE ARE JUST A FEW. The possibilities are endless


@background.task
def work():
    if (time_delay != 0):
        time.sleep(time_delay)
    os.system(commandline+payload)


work()
