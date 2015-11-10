#!/usr/bin/env python
## RPI Alarm
## Author: Nicholas Lau
## github: https://github.com/nmlau/RPiAlarm
## Website: http://www.nicklau.io
from __future__ import print_function

import quickstart

import pdb
import httplib2
import datetime
import pytz
import time

from apiclient import discovery

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = quickstart.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    localFormat = "%Y-%m-%dT%H:%M"

    utcmoment_unaware = datetime.datetime.utcnow()
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)
    
    localDatetime = utcmoment.astimezone(pytz.timezone('America/Los_Angeles'))
    now = localDatetime.strftime(localFormat)
    print(now)

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_short = event['start']['dateTime'][:-9]
        # print(start, event['summary'])
        # pdb.set_trace()
        print(event['summary'])
        print(start_short)
        if (start_short == now):
          print("WAKEUP")
          print("WAKEUP1")
          print("WAKEUP2")
          print("WAKEUP3")
          print("WAKEUP4")
          print("WAKEUP5")

if __name__ == '__main__':
    FREQUENCY_CHECK = 5
    while True:
        main()
        time.sleep(FREQUENCY_CHECK)
