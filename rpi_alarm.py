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

from modules import alarm

if __name__ == '__main__':
  alarm = alarm.Alarm()
  while True:
    alarm.start()
