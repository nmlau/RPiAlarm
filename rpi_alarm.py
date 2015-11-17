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
        self.enable = True
    def run(self):
        try:
            if self.enable == False:
                sleep(self.interval)
            while self.enable:
                events = googlecalendar.get_events(self.credentials)
                now = timezone.getCurrentTimeFromTimeZone(self.timezone)
                if googlecalendar.checkEvents(events, now):
                    sound.soundAlarm(self.mp3_path)
                sleep(self.interval)
        except KeyboardInterrupt:
            # Could use a sleep here, would be super easy and clean: sleep(12 hours)
            self.enable = False

if __name__ == '__main__':
    alarm = Alarm()
    while True:
        alarm.run()