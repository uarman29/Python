from PIL import ImageGrab
import os
import time

def getScreen():
    box = (100,100,500,500)
    im = ImageGrab.grab(box)
    im.show()

getScreen()