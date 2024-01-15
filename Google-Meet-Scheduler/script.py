from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from uuid import uuid4
from typing import Dict, List
import os

SCOPES = ["https://www.googleapis.com/auth/calendar"]


class CreateMeet:
    def __init__(self, attendees: Dict[str, str],
                 event_time: Dict[str, str], Topic):
        authe = self._auth()
        attendees_list = [{"email": e} for e in attendees.values()]
        self.event_states = self._create_event(
            attendees_list, event_time, authe, Topic)

    @staticmethod
    def _create_event(
            attendees: List[Dict[str, str]], event_time, authe: build, TopiC):
        event = {"conferenceData": {"createRequest": {"requestId": f"{uuid4().hex}", "conferenceSolutionKey": {"type": "hangoutsMeet"}}},
                 "attendees": attendees,
                 "start": {"dateTime": event_time["start"], 'timeZone': 'Asia/Kolkata'},
                 "end": {"dateTime": event_time["end"], 'timeZone': 'Asia/Kolkata'},
                 "summary": TopiC,
                 "reminders": {"useDefault": True}
                 }
        event = authe.events().insert(calendarId="primary", sendNotifications=True,
                                      body=event, conferenceDataVersion=1).execute()
        return event

    @staticmethod
    def _auth():
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open("token.json", "w") as token:
                    token.write(creds.to_json())

        service = build("calendar", "v3", credentials=creds)
        return service


print('------------------------------')
print('-- Follow YYYY-MM-DD format --')
print('------------------------------')
date = input('Enter date of the meeting : ').strip()
print('------------------------------------')
print('-- Follow HH:MM and 24 hrs format --')
print('------------------------------------')
start = input('Enter starting time : ').strip()
end = input('Enter ending time : ').strip()
emails = list(
    input('Enter the emails of guests separated by 1 space each : ').strip().split())
topic = input('Enter the topic of the meeting : ')

time = {
    'start': date + 'T' + start + ':00.000000',
    'end': date + 'T' + end + ':00.000000'
}
guests = {email: email for email in emails}
meet = CreateMeet(guests, time, topic)
keys = ['organizer', 'hangoutLink', 'summary', 'start', 'end', 'attendees']
details = {key: meet.event_states[key] for key in keys}
print('---------------------')
print('-- Meeting Details --')
print('---------------------')
for key in keys:
    print(key + ' : ', details[key])
