from googleapiclient.discovery import build
from uuid import uuid4
from google.auth.transport.requests import Request
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from typing import Dict, List
from pickle import load, dump


class CreateMeet:
    def __init__(self, attendees: Dict[str, str], event_time: Dict[str, str], topic):
        authe = self._auth()
        attendees = [{"email": e} for e in attendees.values()]
        self.event_states = self._create_event(
            attendees, event_time, authe, topic)

    @staticmethod
    def _create_event(attendees: List[Dict[str, str]], event_time, authe: build, topic):
        event = {"conferenceData": {"createRequest": {"requestId": f"{uuid4().hex}", "conferenceSolutionKey": {"type": "hangoutsMeet"}}},
                 "attendees": attendees,
                 "start": {"dateTime": event_time["start"], 'timeZone': 'Asia/Kolkata'},
                 "end": {"dateTime": event_time["end"], 'timeZone': 'Asia/Kolkata'},
                 "summary": topic,
                 "reminders": {"useDefault": True}
                 }
        event = authe.events().insert(calendarId="primary", sendNotifications=True,
                                      body=event, conferenceDataVersion=1).execute()
        return event

    @staticmethod
    def _auth():
        token_file, scopes = Path(
            "./token.pickle"), ["https://www.googleapis.com/auth/calendar"]
        credentials = None
        if token_file.exists():
            with open(token_file, "rb") as token:
                credentials = load(token)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', scopes)
                credentials = flow.run_local_server(port=0)
            with open(token_file, "wb") as token:
                dump(credentials, token)
        calendar_service = build("calendar", "v3", credentials=credentials)
        return calendar_service


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
    'start': date+'T'+start+':00.000000',
    'end': date+'T'+end+':00.000000'
}
guests = {email: email for email in emails}
meet = CreateMeet(guests, time, topic)
keys = ['organizer', 'hangoutLink', 'summary', 'start', 'end', 'attendees']
details = {key: meet.event_states[key] for key in keys}
print('---------------------')
print('-- Meeting Details --')
print('---------------------')
for key in keys:
    print(key+' : ', details[key])
