import pyautogui
from mss import mss
from PIL import Image



class Detector(object):
  def __init__(self):
    self.width, self.height = pyautogui.size()
    self.bounding_box = {'top': 0, 'left': 0, 'width': self.width, 'height': self.height}
    self.sct = mss()
  
  def detect(self):
    while True:
      

#  def shortObstacle(self):
