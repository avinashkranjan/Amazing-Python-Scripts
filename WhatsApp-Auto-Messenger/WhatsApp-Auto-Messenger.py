"""
    WhatsApp Auto Messenger
    - Send message to your friend or group by using just 7 lines of Python Script
"""

import pywhatkit
phoneno = input("Enter Receiver(recipient) Phone Number :")
message = input("Enter Message You want to send :")
print("Enter Schedule Time to send WhatsApp message to recipient :")
Time_hrs = int(input("- At What Hour :"))
Time_min = int(input("- At What Minutes :"))
pywhatkit.sendwhatmsg(phoneno, message, Time_hrs, Time_min)

# Tip : Do you want to send and schedule a messages to any WhatsApp group then use below code and provide inside attributes value.

# pywhatkit.sendwhatmsg_to_group(GroupID, message, time_hour, time_min, wait_time)

# Note : Group ID is something that is in its invite link,
