import cv
import time
from rgb_connection import RgbConnection

color_array = [
    (0,0,255),
    (0,255,0),
    (255,0,0)
    ]
t = 50

def check_rgb(rgb):
    max_i = 0
    if rgb[max_i] < rgb[1]:
        max_i = 1
    if rgb[max_i] < rgb[2]:
        max_i = 2
    return max_i

def color_check(img, length):
    px = img.width/2
    py = img.height/2
    minx = max(px-length, 0)
    miny = max(py-length, 0)
    maxx = min(px+length, img.width)
    maxy = min(py+length, img.height)

    color_data = []

    for i in range(minx, maxx):
        for j in range(miny, maxy):
            color_data.append(check_rgb(cv.Get2D(img,i,j)))
            
    max_num = color_data[0]
    max_i = 0
    for i in range(0, len(color_data)):
        if max_num < color_data[i]:
            max_i = i
            max_num = color_data[i]
    if max_i <= 1:
        print color_data[max_i]
    return color_data[max_i]

def printLine(img, length):
    px = img.width/2
    py = img.height/2
    minx = max(px-length, 0)
    miny = max(py-length, 0)
    maxx = min(px+length, img.width)
    maxy = min(py+length, img.height)

    cv.Line(img,(px, miny),(px, maxy), cv.CV_RGB(0,0,0))
    cv.Line(img,(minx, py),(maxx, py), cv.CV_RGB(255,255,255))
    

cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)
connect = RgbConnection()

flag = True

while True:
    if flag:
        img = cv.QueryFrame(capture)
        printLine(img, 10)
        cv.ShowImage("camera", img)
    else :
        img = cv.QueryFrame(capture)
        if connect.push_data(color_check(img, 10)) :
            print connect.get_decode_data()
            flag = True

    key = cv.WaitKey(10)
    
    if key == 27:
        break

    if key == 32:
        flag = False
        connect.start_connection()

exit()
