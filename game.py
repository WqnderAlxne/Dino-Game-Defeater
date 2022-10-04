import threading
import time

import webbrowser
import pyautogui

import mss
import mss.tools

class Game:
  def __init__(self):
    txt = open("loc.txt")
    
    self.x = int(txt.readline())
    self.y = int(txt.readline())
    self.xDin = int(txt.readline())
    self.yDin = int(txt.readline())

    txt.close()

    xMax = 1535
    yMax = 863

    xRatio = 1920 / xMax
    yRatio = 1080 / yMax

    self.x *= xRatio
    self.xDin *= xRatio
    self.y *= yRatio
    self.yDin *= yRatio

    self.x = int(self.x)
    self.y = int(self.y)
    self.xDin = int(self.xDin)
    self.yDin = int(self.yDin)
    
    self.sct = mss.mss()
  
  def start(self):
    webbrowser.open("https://offline-dino-game.firebaseapp.com/")
    time.sleep(1)
    pyautogui.keyDown("space")
    pyautogui.keyUp("space") 

  def survive(self, threads):
    for i in range(threads):
      cacti = threading.Thread(target = self.cactus, args = (self.x, self.y))
      dino = threading.Thread(target = self.dinosaur, args = (self.xDin, self.yDin))

      cacti.start()
      dino.start()

  def cactus(self,x,y):
    while True:
      bbox = (x, y, x+1, y+1)
      pxl1 = self.sct.grab(bbox).pixel(0,0)
      while pxl1 == (255, 255, 255):
        pxl1 = self.sct.grab(bbox).pixel(0,0)
        pass
      pyautogui.keyDown("space")
      #time.sleep(0.25)
      pyautogui.keyUp("space")

      x += 3

  def dinosaur(self,x,y):
    while True:
      bbox = (x, y, x+1, y+1)
      pxl2 = self.sct.grab(bbox).pixel(0,0)
      while pxl2 == (255, 255, 255):
        pxl2 = self.sct.grab(bbox).pixel(0,0)
        pass
      pyautogui.keyDown("space")
      pyautogui.keyUp("space")

      x += 20