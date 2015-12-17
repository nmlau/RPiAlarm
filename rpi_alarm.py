## RPI Alarm
## Author: Nicholas Lau
## github: https://github.com/nmlau/RPiAlarm
## Website: http://www.nicklau.io
#!/usr/bin/env python
# from __future__ import print_function

# used for development. Not needed for normal usage.
import pdb                              
# import logging                                   
# logging.basicConfig(filename='alarm.log', filemode='w')

from modules import googlecalendar
from modules import config
from modules import sound
from modules import timezone
from modules import irinterface

import httplib2

from time import sleep

class Alarm:
    def __init__(self):
        # read config file, initialize sound, oauth with google calendars
        configuration = config.readConfig() # returns (string mp3_path, int interval, string timezone)
        self.mp3_path = configuration[0]
        self.interval = configuration[1]
        self.timezone = configuration[2]
        self.shutoff_interval = configuration[3]
        self.query = configuration[4]

        self.sound = sound.Sound(self.mp3_path)
        self.credentials = googlecalendar.get_credentials()
        self.events = {}
    
    def run(self):
        try:
            self.events = googlecalendar.get_events(self.credentials, self.query)
            self.check_events()
            sleep(self.interval)
        except KeyboardInterrupt:
            self.interrupt()
        except httplib2.ServerNotFoundError:
            print "Internet is down, checking latest list of events"
            self.check_events()
    
    def check_events(self):
        now = timezone.get_current_time(self.timezone)
        if googlecalendar.check_events(self.events, now):
            self.sound.start()

    def interrupt(self):
        print("Alarm turned off: {0} Second Interrupt").format(self.shutoff_interval)
        self.sound.stop()
        sleep(self.shutoff_interval)

if __name__ == '__main__':
    alarm = Alarm()
    while True:
        alarm.run()
