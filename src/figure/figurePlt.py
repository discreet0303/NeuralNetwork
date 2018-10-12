import sys
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np
class figurePlt():
    
    def __init__(self, __WINDOW, maxDataRange, minDataRange):
        sys.stdout.write('import from figurePlt in class\n')
        self.__WINDOW = __WINDOW

        self.__FIG = plt.figure()
        self.__CANVAS = FigureCanvasTkAgg(self.__FIG, master = self.__WINDOW)

        self.__MAX_DATA_RANGE = maxDataRange
        self.__MIN_DATA_RANGE = minDataRange
        self.scalePlt()

        self.__CANVAS.draw()
        self.__CANVAS.get_tk_widget().grid(row = 5, column = 0, columnspan = 7, pady = (15, 15), padx = (25, 25))
        
    def clearPlt(self):
        plt.clf()

    def scalePlt(self):
        plt.xlim(self.__MIN_DATA_RANGE - 1, self.__MAX_DATA_RANGE + 1)
        plt.ylim(self.__MIN_DATA_RANGE - 1, self.__MAX_DATA_RANGE + 1)

    def resetDataRagne(self, maxDataRange, minDataRange):
        self.__MAX_DATA_RANGE = maxDataRange
        self.__MIN_DATA_RANGE = minDataRange
        self.scalePlt()
