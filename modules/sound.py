#!/usr/bin/env python

import os
import random

def soundAlarm(mp3_path):
    print "Waking you up!"
    print "---" 
    songfile = random.choice(os.listdir(mp3_path)) #  choosing by random an .mp3 file from direcotry
    print "Now Playing:", songfile
                                                   #  plays the MP3 in it's entierty. As long as the file is longer 
                                                   #  than a minute it will only be played once:
    command ="mpg123" + " " + mp3_path + "'"+songfile+"'"+ " -g 100" 
    print command
    os.system(command)                             #  plays the song