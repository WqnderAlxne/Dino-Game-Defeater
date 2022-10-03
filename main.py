from game import Game

import threading
import time

import pyautogui

import cv2
import mss
import mss.tools

game = Game()

txt = open("loc.txt")

x = int(txt.readline())
y = int(txt.readline())
xDin = int(txt.readline())
yDin = int(txt.readline())

txt.close()

xMax = 1535
yMax = 863

xRatio = 1920 / xMax
yRatio = 1080 / yMax

x *= xRatio
y *= yRatio
xDin *= xRatio
yDin *= yRatio


x = int(x)
y = int(y)
xDin = int(xDin)
yDin = int(yDin)

def cactus(x,y):
  while True:
    bbox = (x, y, x+1, y+1)
    pxl1 = sct.grab(bbox).pixel(0,0)
    if pxl1 != (255, 255, 255):
        
        pyautogui.keyDown("space")
        #time.sleep(0.25)
        pyautogui.keyUp("space")

        x += 3
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
      cv2.destroyAllWindows()
      break

def dinosaur(x,y):
  # y = 464
  while True:
    bbox = (x, y, x+1, y+1)
    pxl2 = mss.mss().grab(bbox).pixel(0,0)
    if pxl2 != (255, 255, 255):
      pyautogui.keyDown("space")
      pyautogui.keyUp("space")

      x += 20
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
      cv2.destroyAllWindows()
      break

with mss.mss() as sct:
  arr = []

  for i in range(1):
    t1 = threading.Thread(target = cactus, args = (x,y))
    t2 = threading.Thread(target = dinosaur, args = (xDin,yDin))

    arr.append(t1)
    arr.append(t2)
  
  for i in arr:
    i.start()