import os
import re
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Iterable, Optional

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv


# Validate Email
def check_email(email):
    regex = r'(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}'  # DO NOT CHANGE
    return bool(re.match(regex, email))


# Shorten the name if it's too long
def shorten_name(name, max_length):
    split_names = name.split(" ")
    name = ''
    if len(name) > max_length and len(split_names) > 1:
        for i in split_names[:-1]:
            name += i[0] + '.'
        name += ' ' + split_names[-1]

    return name


# Create Certificate
def make_certificate(
        name: str,
        template_file: Optional[str] = None,
        font_file: Optional[str] = None,
        starting_position: Optional[Iterable[int]] = None
):
    if not template_file:
        template_file = os.getenv('CERTIFICATE_TEMPLATE_FILEPATH')

    if not font_file:
        font_file = os.getenv('CERTIFICATE_NAME_FONT_FILEPATH')

    if not starting_position:
        starting_position = tuple(map(int, os.getenv(
            'CERTIFICATE_NAME_STARTING_POSITION').split(',')))

    img = Image.open(template_file)  # CERTIFICATE TEMPLATE
    img.load()
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype(font_file, 96)

    if name != "":
        if len(name) > 20:
            shortened_name = shorten_name(name, 20)
        else:
            shortened_name = name

        # POSITION OF NAME TEXT (Check README FOR TUTORIAL)
        draw.text(starting_position, shortened_name, (0, 0, 0), font=font)
    else:
        return None

    if not os.path.exists('certificates'):
        os.mkdir('certificates')  # CREATE FOLDER

    background = Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])

    # SAVE IN FOLDER
    background.save(f'certificates/{name}.pdf', "PDF", resolution=100.0)

    return 'certificates/' + str(name) + '.pdf'


def send_mail(receiver: str, certificate_filepath: str,
              email_id: Optional[str] = None, pwd: Optional[str] = None,
              subject: Optional[str] = None, body: Optional[str] = None):
    if not email_id:
        email_id = os.getenv('EMAIL_ID')

    if not pwd:
        pwd = os.getenv('EMAIL_PASSWORD')

    if not subject:
        subject = os.getenv('EMAIL_SUBJECT')

    if not body:
        body = os.getenv('CERTIFICATE_EMAIL_BODY')

    # Email Setup
    server = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP SERVER
    server.starttls()  # Traffic encryption
    server.login(email_id, pwd)  # SMTP Login

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_id
    # msg['Reply-to'] = email_id
    msg['To'] = receiver

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'

    # Body
    part = MIMEText(body)
    msg.attach(part)

    # Attachment
    part = MIMEApplication(open(certificate_filepath, "rb").read())
    part.add_header('Content-Disposition', 'attachment',
                    filename=os.path.basename(certificate))
    msg.attach(part)

    # Send Mail
    server.sendmail(email_id, receiver, msg.as_string())


# Run Script
if __name__ == '__main__':
    load_dotenv()
    error_list = []
    error_count = 0

    excel_file = os.getenv('CERTIFICATE_HOLDERS_EXCEL_FILEPATH')

    # Reading File
    file = pd.ExcelFile(excel_file, engine='openpyxl')
    count = 0

    for sheet in file.sheet_names:
        print("\n\n<-- New Sheet -->\n")
        recipient_df = file.parse(sheet)

        for _, row in recipient_df.iterrows():

            recipient_name, recipient_email = row

            if check_email(recipient_email):
                certificate = make_certificate(recipient_name)

                # Successfully made certificate
                if certificate:
                    send_mail(receiver=recipient_email,
                              certificate_filepath=certificate)
                    print(">>> ", count, ": ", recipient_email, " : Sent")
                else:
                    # Add to error list
                    error_list.append(recipient_email)
                    error_count += 1
            else:
                # Add to error list
                error_list.append(recipient_email)
                error_count += 1

            count += 1

    print("\n\n <<:>> All Emails Sent <<:>>\n\n")
    print(f"Error List: {error_list}")
