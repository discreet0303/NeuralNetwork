import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

class figurePlt():
    
    def __init__(self, __WINDOW, maxDataRange, minDataRange):
        self.__WINDOW = __WINDOW

        self.__FIG = plt.figure()
        self.__CANVAS = FigureCanvasTkAgg(self.__FIG, master = self.__WINDOW)

        self.__MAX_DATA_RANGE = maxDataRange
        self.__MIN_DATA_RANGE = minDataRange
        self.scalePlt()

        self.__CANVAS.draw()
        self.__CANVAS.get_tk_widget().grid(row = 4, column = 0, columnspan = 7, pady = (15, 15), padx = (25, 25))

    def clearPlt(self):
        plt.clf()

    def scalePlt(self):
        plt.xlim(self.__MIN_DATA_RANGE, self.__MAX_DATA_RANGE)
        plt.ylim(self.__MIN_DATA_RANGE, self.__MAX_DATA_RANGE)

    def resetDataRagne(self, maxDataRange, minDataRange):
        self.__MAX_DATA_RANGE = maxDataRange
        self.__MIN_DATA_RANGE = minDataRange
        self.scalePlt()

    def updateCanvasForPoint(self, dataSetPoints, maxRangeNum, minRangeNum):
        self.resetDataRagne(int(maxRangeNum) + 2, int(minRangeNum) - 2)
        
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

    def updateCanvasForLine(self, answer, maxRangeNum, minRangeNum):
        # self.scalePlt(maxRangeNum, minRangeNum)

        print('updateCanvas')
        self.resetDataRagne(int(maxRangeNum) + 2, int(minRangeNum) - 2)

        ax = plt.axes()
        x = np.linspace(minRangeNum - 2, maxRangeNum + 2)
        y = answer[0] - answer[1] * x
        ax.plot(x, y)

        self.__CANVAS.draw()