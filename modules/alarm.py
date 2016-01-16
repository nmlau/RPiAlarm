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
        self.configuration = config.readConfig()

        # initialize modules module
        self.sound = sound.Sound(self.configuration['mp3_path'], float(self.configuration['automatic_shutoff_interval']))
        self.credentials = googlecalendar.get_credentials()
        self.events = {} # check whether this declaration is necessary or if can just initialize
    
    def start(self):
        try:
            self.events = googlecalendar.get_events(self.credentials, self.configuration['query'])
            self.check_events()
            sleep(float(self.configuration['polling_interval']))
        
        # IR Remote sends KeyboardInterrupt Signal to shut off Alarm and Lock it
        except KeyboardInterrupt:
            self.lock()

        # Handles Internet Loss
        except httplib2.ServerNotFoundError:
            print "Internet is down, using latest result"
            self.check_events()
    
    def check_events(self):
        now = timezone.get_current_time(self.configuration['timezone'])
        if googlecalendar.check_events(self.events, now):
            print "Alarm Triggered!"
            self.sound.start()

    def lock(self):
        print("Alarm turned off: {0} Second Interrupt").format(int(self.configuration['lock_interval']))
        self.sound.stop()
        sleep(float(self.configuration['lock_interval']))