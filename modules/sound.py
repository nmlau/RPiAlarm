#!/usr/bin/env python

from threading import Thread
from time import sleep

import os
import random
import platform

class Sound:
  def __init__(self, mp3_path, automatic_shutoff_interval):
    self.playing = False  # Since the command plays in background, stops multiple from running
    self.mp3_path = mp3_path
    self.automatic_shutoff_interval = automatic_shutoff_interval
  
  def start(self):
    if self.playing == False:
      command = self.create_command()
      print "Starting Sound: " + command
      self.playing = True
      os.system(command)

      # Automatically shuts off alarm after configured time, magic number for now
      sleep(self.automatic_shutoff_interval)
      self.stop()

    else:
      print "Sound already running"

  def stop(self):
    command = "pkill mpg123"
    print "Stopping Sound: " + command
    self.playing = False
    os.system(command)

  def create_command(self):
    # choosing by random an .mp3 file from direcotry
    songfile = random.choice(os.listdir(self.mp3_path))
    print "Now Playing:", songfile
    
    # check Platform
    if platform.system() == 'Linux':
      command = "mpg321"
    elif platform.system() == 'Darwin':
      command = "mpg123"
      
    # -g 100, sets sound to 100, & runs in background
    #  plays the MP3. As long as the file is longer than a minute it will only be played once
    # command += " -g 100 " + self.mp3_path + "'"+songfile+"'"+ " &"
    # -g flag has been deprecated
    command += ' ' + self.mp3_path + "'"+songfile+"'"+ " &"

    return command
