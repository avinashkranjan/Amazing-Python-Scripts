import requests
from smtplib import SMTP
import os
from dotenv import load_dotenv

load_dotenv()


def function():
    """Go to Manage your Google(or any mail) account, and then headover to Security.\nTurn OFF the options 'Two Step Verification' and 'Use your phone to sign in' in the Signing in to Google section.\nTurn ON the Less secure apps section.
    """
    return 0


print(function.__doc__)
MY_MAIL = os.getenv('MAIL')
MY_PASSWORD = os.getenv('PASSWORD')
RECIEVER_MAIL = input('Send mail to (mail id): ')
CITY = input('Enter your City: ')

API_KEY = os.getenv('API')

API_END_POINT = 'https://nominatim.openstreetmap.org/search.php'
PARAMETER_LOCATION = {
    'city': CITY,
    'format': 'json',
}
response_location = requests.get(url=API_END_POINT, params=PARAMETER_LOCATION)
data_location = response_location .json()
LAT = data_location[0]['lat']
LONG = data_location[0]['lon']
PARAMETER = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}
api = requests.get(
    url="http://api.openweathermap.org/data/2.5/onecall", params=PARAMETER)
data = api.json()

bring_umbrella = False

for i in range(0, 12):
    hourly_condition = data['hourly'][i]['weather'][0]['id']
    if (hourly_condition < 700):
        bring_umbrella = True

if (bring_umbrella == True):
    MESSAGE = f"Subject: Rain Rain \n\nIt's going to rain today. Bring Umbrella "

else:
    MESSAGE = f"Subject: Sunny Day\n\nMay be a sunny day. Carry sunglasses. "

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_MAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_MAIL, to_addrs=RECIEVER_MAIL,
                        msg=MESSAGE)
    print('Mail Sent')
