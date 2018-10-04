
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
        self.drawFigure()

    def drawFigure(self):

        fig = plt.figure()
        ax = plt.axes()

        plt.xlim(-2, 2)
        plt.ylim(-2, 2)

        x = np.linspace(-90, 90)
        ax.plot(x, x)
        
        # x axis value list.
        x_number_list = [0, 0, 1, 1]
        # y axis value list.
        y_number_list = [0, 1, 0, 1]

        # Draw point based on above x, y axis values.
        plt.scatter(x_number_list, y_number_list, s=10)

        # fig = Figure(figsize=(3, 3), dpi=100)
        # t = np.arange(-3, 3, .01)
        # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        canvas = FigureCanvasTkAgg(fig, master=self.__WINDOW)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row = 4, column = 0, columnspan = 5, pady = (15, 15), padx = (25, 25))
        # , sticky=tk.N+tk.S+tk.E+tk.W

    