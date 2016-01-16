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
    config['mp3_path'] = parser.get('alarm', 'mp3_path')
    config['timezone'] = parser.get('alarm', 'timezone')
    config['polling_interval'] = parser.get('alarm', 'polling_interval')
    config['lock_interval'] = parser.get('alarm', 'lock_interval')
    config['automatic_shutoff_interval'] = parser.get('alarm', 'automatic_shutoff_interval')
    config['query'] = parser.get('alarm', 'query')

    return config