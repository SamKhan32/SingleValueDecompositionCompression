from tkinter import *
from tkinter import ttk

cherryPath ="slotGame\\res\cherry.png"
sevenPath = "slotGame\\res\seven.png"
barPath = "slotGame\\res\\bar.png"
class Pane():
    """A window is an object that contains an image represented by a string"""
    image = "bar"
    def setImage(self,image):
        self.image = image        
