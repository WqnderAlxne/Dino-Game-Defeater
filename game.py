import time

import webbrowser
import pyautogui

class Game(object):
  def __init__(self):
    webbrowser.open("https://offline-dino-game.firebaseapp.com/")
    time.sleep(3)
    pyautogui.keyDown("space")
    pyautogui.keyUp("space") 

  def survive(self):
    while True:
      width, height = pyautogui.size()

  def jump(self, duration):
    pyautogui.keyDown("space")
    if duration > 0:
      time.sleep(duration)
    pyautogui.keyDown("space")