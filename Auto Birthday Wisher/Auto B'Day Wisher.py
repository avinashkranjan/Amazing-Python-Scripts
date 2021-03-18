import pandas as pd                                                     # Pandas library is used for importing and reading the data
import datetime                                                         # datetime module is used for fetching the dates
import smtplib															# smtp library used for sending mail
import os

current_path = os.getcwd()
print(current_path)
os.chdir(current_path)                                                  # Changing the Path of the directory in which you are currently working

GMAIL_ID = input("Enter your email: ")                                  # Give your mail here from which you want to send the wishes
GMAIL_PSWD = input("Enter password for your email mentioned above: ")   # Give your mail password


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent: \nSubject: {sub} ,\nMessage: {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)                             # creating server to send mail
    s.starttls()                                                        # start a TLS session
    s.login(GMAIL_ID, GMAIL_PSWD)                                       # the function will login with your Gmail credentials
    s.sendmail(GMAIL_ID, to, f"Subject: {sub} \n\n {msg}")              # sending the mail
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")                                     # the datasheet where the data of the friends is stored
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")

    writeInd = []
    for index, item in df.iterrows():
        bday = item['Birthday']
        bday = datetime.datetime.strptime(bday, "%d-%m-%Y")
        bday = bday.strftime("%d-%m")
        if(today == bday) and yearNow not in str(item['LastWishedYear']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])    # calling the sendmail function
            writeInd.append(index)

    if writeInd != None:
        for i in writeInd:
            oldYear = df.loc[i, 'LastWishedYear']
            df.loc[i, 'LastWishedYear'] = str(oldYear) + ", " + str(yearNow)

    df.to_excel('data.xlsx', index=False)
