import smtplib

to = input("Enter the Email of recipent:\n")
content = input("Enter the Content for E-Mail:\n")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', '12345678')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()


sendEmail(to, content)
