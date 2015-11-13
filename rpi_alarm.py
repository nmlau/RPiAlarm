#!/usr/bin/env python
## RPI Alarm
## Author: Nicholas Lau
## github: https://github.com/nmlau/RPiAlarm
## Website: http://www.nicklau.io
# from __future__ import print_function

import quickstart

import pdb
import httplib2
import datetime
import pytz
from apiclient import discovery

import os
import time
import random
from ConfigParser import SafeConfigParser

import logging                                   # used for development. Not needed for normal usage.
logging.basicConfig(filename='wakeup.log', filemode='w')

def masterControl():
    config = readConfig()

    global mp3_path
    mp3_path = config[0]
    global interval
    interval = config[1]

    while True:
        events = getEvents()
        now = getCurrentTimeFromTimeZone('PST')
        checkEvents(events, now)
        time.sleep(interval)

def readConfig():
    parser = SafeConfigParser()                       # initiate Parser and read the configuration file
    parser.read('config')    

    # email = parser.get('credentials', 'email')
    # password = parser.get('credentials', 'password')
    # query = parser.get('alarm', 'query')
    pdb.set_trace()
    mp3_path = parser.get('alarm', 'mp3_path')
    interval = parser.get('alarm', 'interval')
    # calendar = parser.get('alarm', 'calendar')
    return (mp3_path, int(interval))

def getEvents():
    credentials = quickstart.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    # Get next 10 events
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()

    return eventsResult.get('items', [])

def checkEvents(events, now):
    if not events:
        print('No upcoming events found.')
    for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event['summary'])
        start_short = event['start']['dateTime'][:-9]

        # localFormat = "%Y-%m-%dT%H:%M" 
        # start_short.strftime(localFormat)
        
        print(start_short, event['summary'])
        if (start_short >= now):
          soundAlarm()

def getCurrentTimeFromTimeZone(timezone):
    #same format as google event time
    localFormat = "%Y-%m-%dT%H:%M" 

    utcmoment_unaware = datetime.datetime.utcnow()
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)
    
    if timezone == 'PST':
        localDatetime = utcmoment.astimezone(pytz.timezone('America/Los_Angeles'))
        
    return localDatetime.strftime(localFormat)

def soundAlarm():
    print("BRRINGGG BRINGGGGGG BRIIINGGGGGG")
    print "Waking you up!"
    print "---" 
    songfile = random.choice(os.listdir(mp3_path)) #  choosing by random an .mp3 file from direcotry
    print "Now Playing:", songfile
                                                   #  plays the MP3 in it's entierty. As long as the file is longer 
                                                   #  than a minute it will only be played once:
    command ="mpg123" + " " + mp3_path + "'"+songfile+"'"+ " -g 100" 
    print command
    os.system(command)                             #  plays the song

if __name__ == '__main__':
    masterControl()
