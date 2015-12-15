#!/usr/bin/env python

import os
import random
import platform

class Sound:
  def __init__(self, mp3_path):
    self.playing = False  # Since the command plays in background, stops multiple from running
    self.mp3_path = mp3_path
  
  def start(self):
    if self.playing == False:
      print "Waking you up!"
      print "---" 
      songfile = random.choice(os.listdir(self.mp3_path)) #  choosing by random an .mp3 file from direcotry
      print "Now Playing:", songfile
                                                     #  plays the MP3 in it's entierty. As long as the file is longer 
                                                     #  than a minute it will only be played once:
      # -g 100, sets sound to 100, & runs in background
      if platform.system() == 'Linux':
        command = "mpg321"
      else if platform.system() == 'Darwin':
        command = "mpg123"
      command += " " + self.mp3_path + "'"+songfile+"'"+ " -g 100 &"

      print command
      self.playing = True
      os.system(command)                             #  plays the song

  def stop(self):
    command = "pkill mpg123"
    print command
    self.playing = False
    os.system(command)
