#!/usr/bin/env python
#coding: utf-8

# dotpitch: caculate screen dotpitch
# Author: David Wang (sa.station@gmail.com), 2012/9/2

import math

class DotPitch:
    def __init__(self):
        self.ScreenRatio = 0
        self.xSize = 0
        self.ySize = 0
        self.xDotPitch = 0
        self.yDotPitch = 0

    def Caculate(self, ScreenSize, xPixel, yPixel):
        ScreenSize = float(ScreenSize)
        xPixel = int(xPixel)
        yPixel = int(yPixel)
        
        divisor = self.euclid(xPixel, yPixel)

        self.ScreenRatio  = str(xPixel/divisor) + ":" + str(yPixel/divisor)
        
        ratio = float(xPixel)/float(yPixel)
        self.xSize = math.sqrt(ScreenSize**2/(1+(1/ratio)**2))
        self.ySize = 1/ratio*self.xSize
        self.xDotPitch = self.xSize*25.4/xPixel # 1 inch = 25.4 mm
        self.yDotPitch = self.ySize*25.4/yPixel
    
    # common divisor
    def euclid(self, numA, numB):
        while numB != 0:
            numRem = numA % numB
            numA = numB
            numB = numRem
            
        return numA


if __name__ == '__main__':
    print "Screen size:",
    screensize = input()
    print "X-Pixel:",
    xpixel = input()
    print "Y-Pixel:",
    ypixel = input()

    screen = DotPitch()
    screen.Caculate(screensize, xpixel, ypixel)
    
    print "Screen Ratio: %s" % screen.ScreenRatio
    print "Dot Pitch: %.4f mm" % screen.xDotPitch
    print "X Size: %.1f inch" % screen.xSize
    print "Y Size: %.1f inch" % screen.ySize
    
