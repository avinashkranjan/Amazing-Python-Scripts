import pywhatkit

"""
To find Group_ID: Copy from WhatsApp group join link
"""

Group_ID = input("Enter WhatsApp Group ID:")
Message = input("Enter Message You want to send :")
print("Enter Schedule Time to send WhatsApp message to recipient :")
Time_hrs = int(input("- At What Hour :"))
Time_min = int(input("- At What Minutes :"))
pywhatkit.sendwhatmsg_to_group(Group_ID, Message, Time_hrs, Time_min)
