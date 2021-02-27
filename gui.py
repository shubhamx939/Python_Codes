#importing numpy and pandas
import pandas as pd 
import numpy as np 

#import tkinter package
from tkinter import *

from mywindow import LRwindow

window = Tk()      #Creating a window for the GUI

lrw = LRwindow(window)

window.title("Californian Housing Price Prediction")        #Title of the window

window.mainloop()       #To make the GUI window Alive or openable until user closes it



