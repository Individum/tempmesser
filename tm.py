#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, time

# function: read and parse sensor data file
def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except (IOError):
    print(time.strftime("%x %X"), "Error reading", path)
  return value

f = open("temperaturen.txt", "a")
while (True):
    value = read_sensor("/sys/bus/w1/devices/28-000005aa20e6/w1_slave")
    f.write(value + " °C\n")
    time.sleep(10)
f.close()
