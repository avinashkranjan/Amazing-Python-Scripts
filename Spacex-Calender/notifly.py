from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# Enter your own Google Calendar API json credentials file below (if you renamed it)
api_credentials_json = 'credentials.json'

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

MONTH_MAP = {
    "january": 1,
    "jan": 1,
    "february": 2,
    "feb": 2,
    "march": 3,
    "mar": 3,
    "april": 4,
    "apr": 4,
    "may": 5,
    "june": 6,
    "jun": 6,
    "july": 7,
    "jul": 7,
    "august": 8,
    "aug": 8,
    "september": 9,
    "sept": 9,
    "sep": 9,
    "october": 10,
    "oct": 10,
    "november": 11,
    "nov": 11,
    "december": 12,
    "dec": 12
}


def google_calendar_setup():
    """
    Sets up the Google Calendar API and returns the calendar object service
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                api_credentials_json, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def is_in_current_month(date, current_month) -> bool:
    """
    Returns true if the launch is in the current/desired month
    """
    # find month of rocket launch to make sure it is in current month
    date_split = date.split()
    launch_month = date_split[1].strip().lower()
    launch_month_split = launch_month.split(',')

    if (MONTH_MAP[launch_month_split[0]] == current_month):
        return True
    return False


def create_calendar(service) -> str:
    """ 
    Creates a new calendar to add rocket launch events to
    and returns the calendar's ID
    """
    launch_calendar = {
        'summary': 'Rocket launches by Notifly',
        'timeZone': 'America/New_York'
    }

    calendars = service.calendarList().list().execute()
    calendarId = ""

    exists = False
    for calendar in calendars['items']:
        # print(calendar['summary'])
        if (calendar['summary'] == 'Rocket launches by Notifly'):
            exists = True
            calendarId = calendar['id']
            break

    if (not exists):
        notifly_calendar = service.calendars().insert(body=launch_calendar).execute()
        print(
            f"Calendar {notifly_calendar['summary']} was successfully created")
        calendarId = notifly_calendar['id']

    return calendarId


def add_to_calendar(title, date, location, service, notifly_calendar_id) -> bool:
    """
    Creates an event with the rocket launch information and adds it 
    to Notifly's calendar. Returns false if the event already exists
    """
    if (get_utc_time(date) != "all day"):
        start_launch_time = get_utc_time(date)
        added_hour = str(int(start_launch_time[1])+1)
        if (start_launch_time[0] == '2' and added_hour == '4'):
            end_launch_time = '23:59'
        elif (int(start_launch_time[0]) > 0):
            end_launch_time = start_launch_time[0] + \
                added_hour + start_launch_time[2:]
        else:
            end_launch_time = '0' + added_hour + start_launch_time[2:]

        launch_day = get_launch_date_formatted(date)

        launch_event = {
            'summary': title,
            'location': location,
            'description': 'Rocket launch input by Notifly',
            'start': {
                'dateTime': f'{launch_day}T{start_launch_time}:00Z',
                'timeZone': 'America/New_York',
            },
            'end': {
                'dateTime': f'{launch_day}T{end_launch_time}:00Z',
                'timeZone': 'America/New_York',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 60},
                ],
            },
        }
        # print(start_launch_time)
        # print(end_launch_time)
    else:
        launch_day = get_launch_date_formatted(date)

        launch_event = {
            'summary': title,
            'location': location,
            'description': 'Rocket launch day is not yet determined for this month',
            'start': {
                'date': launch_day,
            },
            'end': {
                'date': launch_day,
            },
        }

    # print(launch_day)

    events = service.events().list(calendarId=notifly_calendar_id).execute()
    event_exists = False

    for old_event in events['items']:
        # replace event with newer version
        if (old_event['summary'] == launch_event['summary']):
            service.events().delete(calendarId=notifly_calendar_id,
                                    eventId=old_event['id']).execute()
            service.events().insert(calendarId=notifly_calendar_id, body=launch_event).execute()
            event_exists = True

    if (not event_exists):
        service.events().insert(calendarId=notifly_calendar_id, body=launch_event).execute()
        return True
    return False


def get_utc_time(launch_date) -> str:
    """
    Returns the rocket launch time in UTC, or all day if the time is NET
    """
    split_date = launch_date.split()
    if (split_date[0] == "NET"):
        return "all day"
    else:
        utc_time = split_date[4]
        return utc_time


def get_launch_date_formatted(launch_date) -> str:
    """
    Returns a date in the formatted form yyyy-mm-dd to be input into as an event date
    """
    split_date = launch_date.split()

    if (len(split_date) < 4):
        month_int = MONTH_MAP[split_date[1].split(',')[0].lower()]
        formatted_date = f"{split_date[2]}-{0 if month_int < 10 else ''}{month_int}-01"
    else:
        month_int = MONTH_MAP[split_date[1].lower()]
        day_without_comma = split_date[2].split(',')[0]

        formatted_date = f"{split_date[3]}-{0 if month_int < 10 else ''}{month_int}-{day_without_comma}"

    return formatted_date


def main(current_month):
    """
    Parses through the nextspaceflight website for upcoming rocket launches and
    adds them to Google Calendar
    """
    service = google_calendar_setup()
    next_page = True
    query_page = 0

    while (next_page):

        # GET HTTP request
        query_page += 1
        response = requests.get(
            'https://nextspaceflight.com/launches/?page=' + str(query_page))

        soup = BeautifulSoup(response.text, 'html.parser')

        notifly_calendar_id = create_calendar(service)

        events_added = 0
        events_updated = 0

        # Determine the first rocket launch that falls under the current month
        start_index = 0
        for grid in soup.find_all(class_='mdl-cell mdl-cell--6-col'):
            date_location = grid.find(
                class_='mdl-card__supporting-text').get_text().split('\n')
            launch_date = date_location[2].strip()

            if (is_in_current_month(launch_date, current_month)):
                break
            start_index += 1

        for grid in soup.find_all(class_='mdl-cell mdl-cell--6-col')[start_index:]:

            # Loop through each launch and check if date is current month
            # Pluck each rocket launch event title, date, and location for the launches
            # in the current month

            launch_title = grid.find(class_='header-style').get_text().strip()
            date_location = grid.find(
                class_='mdl-card__supporting-text').get_text().split('\n')
            launch_date = date_location[2].strip()
            launch_location = date_location[4].strip()

            # stop finding launches once they are outside of the current month
            if (not is_in_current_month(launch_date, current_month)):
                next_page = False
                break

            # print(
            #     f'title: {launch_title} \ndate: {launch_date} \nlocation: {launch_location}')

            # -------Add launch to Google Calendar----------
            if (add_to_calendar(launch_title, launch_date,
                                launch_location, service, notifly_calendar_id)):
                events_added += 1
                print(str(events_added) + " events added")
            else:
                events_updated += 1
                print(str(events_updated) + " events updated")

        print(f'{events_added} events were added from this page')
        print(f'{events_updated} events were updated from this page')


def delete_all():
    """
    Deletes the Notifly rocket launch calendar from Google Calendar
    """
    service = google_calendar_setup()
    notifly_calendar_id = create_calendar(service)

    service.calendarList().delete(                  # pylint: disable=maybe-no-member
        calendarId=notifly_calendar_id).execute()

    print("All events have been deleted, along with the Notifly calendar")


def delete_events(month):
    """
    Deleted rocket launches from the calendar for a specific month
    """

    month_int = MONTH_MAP[month.lower()]

    service = google_calendar_setup()
    notifly_calendar_id = create_calendar(service)

    events = service.events().list(                 # pylint: disable=maybe-no-member
        calendarId=notifly_calendar_id).execute()

    events_deleted = 0

    for event in events['items']:
        # replace event with newer version
        try:
            event_month = int(event['start']['dateTime'].split('-')[1])
        except:
            event_month = int(event['start']['date'].split('-')[1])

        if (event_month == month_int):
            service.events().delete(calendarId=notifly_calendar_id,    # pylint: disable=maybe-no-member
                                    eventId=event['id']).execute()
            events_deleted += 1
            print(f"{events_deleted} events deleted")

    print(str(events_deleted) + " events were deleted")


def button_activated(current_month):
    """
    Runs main method when GUI button is pressed
    """
    main(current_month)


if __name__ == '__main__':
    current_month = datetime.today().month
    main(current_month)
