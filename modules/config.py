#!/usr/bin/env python

from ConfigParser import SafeConfigParser

def readConfig():
    parser = SafeConfigParser()                       # initiate Parser and read the configuration file
    parser.read('config')    

    mp3_path = parser.get('alarm', 'mp3_path')
    interval = parser.get('alarm', 'interval')
    timezone = parser.get('alarm', 'timezone')
    # query = parser.get('alarm', 'query')
    return (mp3_path, int(interval), timezone)
