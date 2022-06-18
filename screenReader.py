from re import S
from turtle import Screen
import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui
import sys
import time

class ScreenReader:
    def __init__(self):
        self.screen = mss()
        #get corner positions of the minesweeper field
        input("Top left corner")
        self.x1, self.y1 = pyautogui.position()
        input("Bottom right corner")
        self.x2, self.y2 = pyautogui.position()
        input("Reset button")
        self.xr, self.yr = pyautogui.position()
        #width and height of field (game coordinates)
        self.sqWidth = int(input("Width: "))
        self.sqHeight = int(input("Height: "))
        self.mSweep = {"top": self.y1, "left": self.x1,
             "width": self.x2-self.x1, "height": self.y2-self.y1}
        #map displays 

        self.map = np.zeros((self.sqHeight,self.sqWidth))
        self.sqWidthPX = int((self.x2-self.x1)/self.sqWidth)
        self.sqHeightPX = int((self.y2-self.y1)/self.sqHeight)

    def parse(self, ignore):
        self.img = np.array(self.screen.grab(self.mSweep))[..., :3]
        import pdb; pdb.set_trace()
        #self.img = Image.frombytes("RGB", self.img.size, self.img.bgra, "raw", "BGRX")
        self.m1 = np.logical_and(
                self.img > np.ones_like(self.img)*np.array([50,30,40]), 
                self.img < np.ones_like(self.img)*np.array([200,80,240])
        ).any()
            
        # for i in range(self.sqHeight):
        #     for j in range(self.sqWidth):
        #         if not ignore[i,j]:
        #             self.m1 = cv2.inRange(self.img[i*self.sqHeightPX:(i+1)*self.sqHeightPX, 
        #                 j*self.sqWidthPX:(j+1)*self.sqWidthPX], np.array([50,50,50]), np.array([200,200,200]))

s = ScreenReader()
s.parse(s.map)
cv2.imshow('screen',np.array(s.img))
cv2.waitKey(0)