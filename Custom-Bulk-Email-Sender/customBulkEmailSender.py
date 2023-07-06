from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import xlrd
import time
import smtplib

path = "selects.xlsx"
File = xlrd.open_workbook(path)
sheet = File.sheet_by_name('Selects')

mail_list = []
interviewerlist = []
name = []
for k in range(sheet.nrows - 1):
    student = sheet.cell_value(k + 1, 0)
    email = sheet.cell_value(k + 1, 1)
    passed = sheet.cell_value(k + 1, 3)
    interviewer = sheet.cell_value(k + 1, 4)
    if passed == 'Yes':
        mail_list.append(email)
        interviewerlist.append(interviewer)
        name.append(student)

email = 'example@gmail.com'  # add the sender's email address
password = '*****'  # sender's password
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

for mail_to in mail_list:
    send_to_email = mail_to
    find_des = mail_list.index(send_to_email)
    studentName = name[find_des]
    subject = f'Congratulations {studentName}!! You are selected for further interviews.'
    message = f'Dear {studentName}, \n' \
              f'We inform you that you wil be interviewed by ${interviewerlist[find_des]}. Please wait for the concern mail from your interviewer. \n'\
              '\n' \
              'Best Regards'

    msg = MIMEMultipart()
    msg['From '] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    print(f'Sending email to {studentName}... ')
    server.sendmail(email, send_to_email, text)

server.quit()
print('Mails sent!')
time.sleep(10)
