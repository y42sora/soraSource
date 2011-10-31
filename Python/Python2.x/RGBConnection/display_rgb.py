# -*- coding: utf-8 -*-
'''
Created on 2011/09/21

@author: y42sora
'''
import cv
import time


color_array = [
    (0,0,255),
    (0,255,0),
    (255,0,0)
    ]
t = 50


class DisplayRGB(object):
 '''
 rgbを表示するクラス
 '''
 width = 400
 height = 400

 def __init__(self):
  self.img = cv.CreateImage ((self.width, self.height), cv.IPL_DEPTH_8U, 3)
  cv.Rectangle(self.img, (0,0), (self.width, self.height), cv.CV_RGB(0,0,255))

 def show(self, col):
  point_list = [[(0, 0), (self.width, 0), (self.width, self.height), (0, self.height)]]
  cv.FillPoly(self.img, point_list, cv.CV_RGB(color_array[col][0], color_array[col][1], color_array[col][2]))
  cv.ShowImage("test", self.img)






		
