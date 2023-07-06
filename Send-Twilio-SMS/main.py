# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Create Virtual Twilio Number (Trail Account)
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"

# Verify Your Personal Phone Number with Twilio (Trail Account)
VERIFIED_NUMBER = "your own phone number verified with Twilio"

# Your Account Sid and Auth Token from twilio.com/console
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# Create Client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Send SMS
message = client.messages \
    .create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_=VIRTUAL_TWILIO_NUMBER,
        to=VERIFIED_NUMBER
    )

# Get Response
print(message.sid)
