import pandas as pd
import smtplib
from email.message import EmailMessage
import xlrd
import openpyxl
import time

# Variable Declarations
excelFile = "DemoExcelFile.xlsx"  # Email Data
emailID = "abc@gmail.com"  # Add MailID
pwd = "abc@7"  # Add PASSWORD
subject = "We're Back!, Walk With World KITCOEK"  # EMAIL SUBJECT
htmlfile_loc = "camp1.html"  # YOUR HTML FILE

# Reading File
file = pd.ExcelFile(excelFile, engine='openpyxl')

# Email Setup
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()  # Traffic encryption
s.login(emailID, pwd)  # SMTP Login
count = 0

for sheet in file.sheet_names:
    print("\n\n<-- New Sheet -->\n")
    df1 = file.parse(sheet)
    for i in range(len(df1['EMAIL'])):

        with open(htmlfile_loc, 'r', encoding='utf8') as file:
            html_Content = str(file.read())
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = emailID
        msg['To'] = df1['EMAIL'][i]
        msg.add_alternative(html_Content, subtype="html")
        s.send_message(msg)
        count += 1
        print(">>> ", df1['SRNO'][i], ": ", df1['EMAIL'][i], " : Sent")
        if (count % 60 == 0):
            print("\n\n <<>> Server CoolDown for 60 seconds <<>>\n\n")
            time.sleep(10)

s.quit()
print("\n\n <<:>> All Emails Sent <<:>>\n\n")
