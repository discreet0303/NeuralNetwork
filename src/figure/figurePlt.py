import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

class figurePlt():
    
    def __init__(self, __WINDOW, maxDataRange, minDataRange, column, figTitle):
        self.__WINDOW = __WINDOW

        self.__FIG = plt.figure(num=1, figsize=(5, 5), dpi=80)
        self.__FIG_TITLE = figTitle
        self.__FIG.suptitle(self.__FIG_TITLE, fontsize = 20)
        
        self.__CANVAS = FigureCanvasTkAgg(self.__FIG, master = self.__WINDOW)

        self.__MAX_DATA_RANGE = maxDataRange
        self.__MIN_DATA_RANGE = minDataRange
        self.scalePlt()

        self.__CANVAS.draw()
        self.__CANVAS.get_tk_widget().grid(row = 5, column = column, columnspan = 6)

    def clearPlt(self):
        plt.clf()
        self.__FIG.suptitle(self.__FIG_TITLE, fontsize = 20)

    def scalePlt(self):
        plt.xlim(self.__MIN_DATA_RANGE - 1, self.__MAX_DATA_RANGE + 1)
        plt.ylim(self.__MIN_DATA_RANGE - 1, self.__MAX_DATA_RANGE + 1)

    def resetDataRagne(self, maxDataRange, minDataRange):
        self.__MAX_DATA_RANGE = maxDataRange
        self.__MIN_DATA_RANGE = minDataRange
        self.scalePlt()

    def updateCanvasForPoint(self, dataSetPoints, testDataIndex):
        self.resetDataRagne(int(self.__MAX_DATA_RANGE), int(self.__MIN_DATA_RANGE))
        
        traingCount = int((len(dataSetPoints) / 3) * 2 + 1)
        count = 1

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
            
            if count - 1 in testDataIndex:
                mark = 'x'
                color = 'k'
            else:
                mark = '.'
            

            plt.scatter(point[0], point[1], s = 20, c = color, marker = mark)
            # if count > traingCount:
            #     plt.scatter(point[0], point[1], s = 20, c = color, marker = mark)
            # else:
            #     plt.scatter(point[0], point[1], s = 20, c = color, marker = mark)
            count += 1

        self.__CANVAS.draw()
        self.__CANVAS.get_tk_widget().grid(row = 5, column = 0, columnspan = 6)

    def updateCanvasForLine(self, answer):
        self.resetDataRagne(int(self.__MAX_DATA_RANGE), int(self.__MIN_DATA_RANGE))

        ax = plt.axes()
        x = np.linspace(self.__MIN_DATA_RANGE - 2, self.__MAX_DATA_RANGE + 2)
        y = answer[0] - answer[1] * x
        ax.plot(x, y)

        self.__CANVAS.draw()
        self.__CANVAS.get_tk_widget().grid(row = 5, column = 0, columnspan = 6)