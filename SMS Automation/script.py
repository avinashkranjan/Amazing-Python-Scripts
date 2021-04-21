from twilio.rest import Client

api = input("Enter your ACCOUNT SID: ")
auth = input("Enter your AUTH TOKEN: ")
from_number = input("Enter number from which you want to send the SMS: ")
message = input("Enter the massage: ")
to_number = input(
    "Enter comma separated numbers to which you want to send the SMS: ")
lists = to_number.split(",")
groupnum = []
for i in lists:
    groupnum.append(i)

account_sid = api
auth_token = auth
client = Client(account_sid, auth_token)

for i in range(len(groupnum)):
    client.messages.create(from_=from_number, body=message, to=groupnum[i])
