#!/usr/bin/env python
import lirc

class IRInterface:
  def __init__(self): pass
  def readIRCode(self):
    sockid = lirc.init("myprogram")
    print("Ready")

    while True:
      code = lirc.nextcode()
      if code: print(code[0])
