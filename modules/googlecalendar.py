#!/usr/bin/env python
from __future__ import print_function
import os

import datetime
import pytz

import httplib2
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_events(credentials, query):
    # credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    # API for events().list at: https://developers.google.com/google-apps/calendar/v3/reference/events/list
    #  enables creation of repeating events
    eventsResult = service.events().list(
        calendarId='primary', q=query, timeMin=now, maxResults=100, singleEvents=True, orderBy='startTime').execute()

    return eventsResult.get('items', [])

def check_events(events, now):
    if not events:
        print('No upcoming events found.')
    for event in events:
        # no dateTime if it's a fullday event (can't select for this in calendar query)
        if not event['dateTime']:
            continue
        # Cut the time to match: localFormat = "%Y-%m-%dT%H:%M"
        start = event['start']['dateTime'][:-9]         
        print(start, event['summary'])
        if (start >= now):
          return True
