import smtplib
from datetime import datetime
import time

# asking for credentials
email_user = input("Enter your email")
email_pass = input("Enter your password")
email_to = input("Enter reciver's email")
email_time = input("Enter time in (YYYY,MM,DD,HH,MM)")
email_message = input("Enter message")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_user, email_pass)

# determining delay
current_time = datetime.now()
email_time = datetime(email_time)
wait_time = (email_time - current_time).total_seconds()
if wait_time > 0:
    time.sleep(wait_time)

# sending email
server.sendmail(email_user, email_to, email_message)
server.quit()
