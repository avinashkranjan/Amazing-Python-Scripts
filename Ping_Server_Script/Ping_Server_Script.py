from twilio.rest import Client
from telethon import TelegramClient
import requests
from telethon.tl.types import InputPeerChat
from telethon.tl.functions.messages import ImportChatInviteRequest

# Define your API credentials
api_id =
api_hash = '######################'

# Twilio API credentials
account_sid = '###############'
auth_token = '################'
twilio_client = Client(account_sid, auth_token)

# Telegram API client setup
telegram_client = TelegramClient('session_name', api_id, api_hash)
telegram_client.start()


def send_telegram_message(chat_id, message):
    chat = InputPeerChat(chat_id)
    telegram_client.send_message(chat, message)


def send_twilio_sms(to_phone_number, message):
    twilio_client.messages.create(
        to=to_phone_number, from_='##########', body=message)


def make_twilio_call(to_phone_number):
    twilio_client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml', to=to_phone_number, from_='#############')


def check_sites(site_list, chat_id):
    for site in site_list:
        print(site)
        r = requests.head(site)
        if r.status_code == 200:
            message = site + " returned 200"
            send_telegram_message(chat_id, message)
            sms_message = "The " + site + " is not responding now"
            send_twilio_sms("#####", sms_message)
            make_twilio_call('############')
        else:
            message = "Oops " + site + " not available at the moment"
            send_telegram_message(chat_id, message)


if __name__ == '__main__':
    # Define the site list and chat ID here
    site_list = ['http://example.com', 'http://example2.com']
    chat_id = 123456789  # Replace with the actual chat ID
    check_sites(site_list, chat_id)
