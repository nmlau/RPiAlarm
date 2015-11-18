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

from time import sleep

class Alarm:
    def __init__(self):
        configuration = config.readConfig() # returns (string mp3_path, int interval)
        self.mp3_path = configuration[0]
        self.interval = configuration[1]
        self.timezone = configuration[2]
        self.credentials = googlecalendar.get_credentials()
        self.sound = sound.Sound(self.mp3_path)
    def run(self):
        try:
            events = googlecalendar.get_events(self.credentials)
            now = timezone.getCurrentTimeFromTimeZone(self.timezone)
            if googlecalendar.checkEvents(events, now):
                self.sound.soundAlarm()
            sleep(self.interval)
        except KeyboardInterrupt:
            # Temporary Hack: 60 Seconds * 60 Minutes * 12 Hours
            self.sound.turnOffAlarm()
            print "KeyboardInterrupt: 12 Hour Shutoff"
            # sleep(60 * 60 * 12) 
            sleep(self.interval * 12)

if __name__ == '__main__':
    alarm = Alarm()
    while True:
        alarm.run()