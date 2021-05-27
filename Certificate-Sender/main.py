import pandas as pd
import smtplib
import re
import os
import openpyxl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# Mail Setup
emailID = "abc1234@gmail.com"  # ADD MAIL ID
pwd = "xyz@1234"  # ADD PASSWORD
subject = "🥳 Thank You For Attending! Here is your Certificate 🎉"  # EMAIL SUBJECT
body = """Hi!\n\nThanks for your active participation in our webinar on "All About Git, GitHub & Open Source" 
Organized by Dhanraj. So now your wait is over and here is your certificate of participation in the webinar.\n\nAlso, 
don't forget to tag on LinkedIn with your certificate. we are happy to see you there!\n\nDhanraj: 
https://www.linkedin.com/in/dhanrajdc7/ """

# Files
excelFile = "Data.xlsx"  # DATA(NAME & EMAIL)
templateFile = "template.png"  # CERTIFICATE TEMPLATE
fontFile = "OpenSans-Bold.ttf"  # FONT
startingPosition = (811, 883)  # POSITION OF NAME TEXT (Check README FOR TUTORIAL)

# Validate Email
def checkMail(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' # DO NOT CHANGE

    if (re.search(regex, email)):
        return True
    else:
        return False


# Shorten the name if it's too long
def shorten( text, _max ):
    t = text.split(" ")
    text = ''
    if len(t)>1:
        for i in t[:-1]:
            text += i[0] + '.'
    text += ' ' + t[-1]
    if len(text) < _max :
        return text
    else :
        return -1

# Create Certificate
def makeCertificate(name):
    img = Image.open(templateFile) # CERTIFICATE TEMPLATE
    img.load()
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype(fontFile, 96)

    if name != "":
        shortTxt = ""
        if len(name) > 20:
            shortTxt = shorten(name, 20)
        else:
            shortTxt = name

        draw.text(startingPosition, shortTxt, (0, 0, 0), font=font) # POSITION OF NAME TEXT (Check README FOR TUTORIAL)
    else:
        return -1

    if not os.path.exists('certificates'):
        os.makedirs('certificates') # CREATE FOLDER

    background = Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])

    background.save('certificates/' + str(name) + '.pdf', "PDF", resolution=100.0) # SAVE IN FOLDER
    return 'certificates/' + str(name) + '.pdf'


def sendMail(fileName, receiver):
    # Email Setup
    server = smtplib.SMTP("smtp.gmail.com", 587) # SMTP SERVER
    server.starttls()  # Traffic encryption
    server.login(emailID, pwd)  # SMTP Login

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = emailID
    # msg['Reply-to'] = emailID
    msg['To'] = receiver

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'

    # Body
    part = MIMEText(body)
    msg.attach(part)

    # Attachment
    part = MIMEApplication(open(filename, "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
    msg.attach(part)

    # Send Mail
    server.sendmail( emailID, receiver, msg.as_string() )


# Run Script
if __name__ == '__main__':
    error_list = []
    error_count = 0

    # Reading File
    file = pd.ExcelFile(excelFile, engine='openpyxl')
    count = 0

    for sheet in file.sheet_names:
        print("\n\n<-- New Sheet -->\n")
        df1 = file.parse(sheet)
        for i in range(len(df1['EMAIL'])):

            if checkMail(df1['EMAIL'][i]):
                filename = makeCertificate(df1['NAME'][i])

                # Successfully made certificate
                if filename != -1:
                    sendMail(filename, df1['EMAIL'][i])
                    print(">>> ", count, ": ", df1['EMAIL'][i], " : Sent")
                    # Add to error list
                else:
                    error_list.append(df1['EMAIL'](i))
                    error_count += 1
            else:
                error_list.append(str(df1['EMAIL'][i]))
                error_count += 1

            count += 1

    print("\n\n <<:>> All Emails Sent <<:>>\n\n")
    print("Error List: " + str(error_list))
