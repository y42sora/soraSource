# -*- coding: utf-8 -*-

import cv
import time
from display_rgb import DisplayRGB
from rgb_connection import RgbConnection

cv.NamedWindow("test", 1)
rg = DisplayRGB()
connect = RgbConnection()

input_file = open("data.txt")

data_list = []
for data in input_file:
 for i in range(len(data)-1):
  data_list.append(connect.toConnectionData(connect.toBinary2(ord(data[i]))))
  print connect.toConnectionData(connect.toBinary2(ord(data[i])))

key = 0
while(True):
 print "init"
 rg.show(2)
 while cv.WaitKey(10) != 32: pass

 print "start"
 for sendData in data_list:
  print "start"
  for sendChar in sendData:
   print sendChar
   rg.show(int(sendChar))
   key = cv.WaitKey(700)
   if key == 27: exit()
   
  print "end"
 print "end"

exit()
