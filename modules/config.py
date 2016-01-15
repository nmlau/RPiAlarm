#!/usr/bin/env python

from ConfigParser import SafeConfigParser

def readConfig():
    parser = SafeConfigParser()                       # initiate Parser and read the configuration file
    parser.read('config')    

    # mp3_path = parser.get('alarm', 'mp3_path')
    # interval = parser.get('alarm', 'interval')
    # timezone = parser.get('alarm', 'timezone')
    # shutoff_interval = parser.get('alarm', 'shutoff_interval')
    # query = parser.get('alarm', 'query')
    # return (mp3_path, int(interval), timezone, int(shutoff_interval), query)

    config = {}
    config["mp3_path"] = parser.get('alarm', 'mp3_path')
    config["interval"] = parser.get('alarm', 'interval')
    config["timezone"] = parser.get('alarm', 'timezone')
    config["shutoff_interval"] = parser.get('alarm', 'shutoff_interval')
    config["query"] = parser.get('alarm', 'query')

    return config