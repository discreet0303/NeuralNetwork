import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

class figurePlt():
    
    def __init__(self, __WINDOW):
        self.__WINDOW = __WINDOW

        self.__FIG = plt.figure()
        self.__CANVAS = FigureCanvasTkAgg(self.__FIG, master = self.__WINDOW)

        self.initPlt()
        self.__CANVAS.draw()
        self.__CANVAS.get_tk_widget().grid(row = 4, column = 0, columnspan = 7, pady = (15, 15), padx = (25, 25))


    def initPlt(self):
        plt.clf()
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)

    def updateCanvasForPoint(self, dataSetPoints, maxRangeNum, minRangeNum):

        plt.clf()
        maxRangeNum = int(maxRangeNum) + 2
        minRangeNum = int(minRangeNum) - 2
        plt.xlim(minRangeNum, maxRangeNum)
        plt.ylim(minRangeNum, maxRangeNum)
        
        for point in dataSetPoints:
            if point[2] == 0:
                color = 'b'
            elif point[2] == 1:
                color = 'g'
            elif point[2] == 2:
                color = 'r'
            elif point[2] == 3:
                color = 'c'
            elif point[2] == 4:
                color = 'm'
            else:
                color = 'g'

            plt.scatter(point[0], point[1], s = 10, c = color)

        self.__CANVAS.draw()

    def updateCanvasForLine(self):

        print('updateCanvas')
        self.initPlt()

        x_number_list2 = [1, 1, 1.5, 1.5]
        y_number_list2 = [0, 1, 0, 1]

        plt.scatter(x_number_list2, y_number_list2, s=10)

        self.__CANVAS.draw()