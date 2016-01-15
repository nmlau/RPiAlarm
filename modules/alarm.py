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
        self.configuration = config.readConfig() # returns (string mp3_path, int interval, string timezone)
        # self.mp3_path = configuration[0]
        self.interval = float(self.configuration['interval'])
        self.timezone = self.configuration['timezone']
        self.shutoff_interval = int(self.configuration['shutoff_interval'])
        self.query = self.configuration['query']

        self.sound = sound.Sound(self.configuration['mp3_path'])
        self.credentials = googlecalendar.get_credentials()
        self.events = {} # check whether this declaration is necessary or if can just initialize
    
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