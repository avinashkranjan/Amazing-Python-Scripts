import requests
from smtplib import SMTP

#turn off certain security criteria in sender mail address
MY_MAIL= ENTER_YOUR_MAIL
MY_PASSWORD= ENTER_YOUR_PASSWORD
RECIEVER_MAIL = RECIEVER_MAIL
#get latitude longitude from  "https://www.latlong.net/"
LAT = 22.572645
LONG = 88.363892

API_KEY = API

PARAMETER= {
    "lat": LAT,
    "lon": LONG,
    "appid" : API_KEY,
    "exclude" : "current,minutely,daily",
}
api = requests.get(url="http://api.openweathermap.org/data/2.5/onecall",params=PARAMETER)

data =  api.json()
print(data)

bring_umbrella = False

for i in range(0,12):
    hourly_condition = data['hourly'][i]['weather'][0]['id']
    if(hourly_condition<700):
        bring_umbrella = True

if (bring_umbrella == True):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=RECIEVER_MAIL,
                            msg=f"Subject: Rain Rain \n\nIt's going to rain today. Bring Umbrella ")
        print('Mail Sent')
else:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs='shubhrijana@gmail.com',
                            msg=f"Subject: Sunny Day\n\nMay be a sunny day. Carry sunglasses. ")
        print('Mail Sent')



