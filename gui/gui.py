import tkinter as tk
import os

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


class GUI: 

    __WINDOW = tk.Tk()

    def __init__(self):
        self.__WINDOW.title("Neural Network HW_01")
        self.__WINDOW.resizable(0, 0)
        self.__WINDOW.geometry("600x600+500+300")

        self._component()
        self.plt()

        self.__WINDOW.mainloop()

    def plt(self):
        fig = Figure(figsize=(2, 2), dpi=100)
        t = np.arange(-3, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        canvas = FigureCanvasTkAgg(fig, master=self.__WINDOW)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row = 4, column = 0, columnspan = 3, pady = (15, 15), padx = (25, 25))
        # , sticky=tk.N+tk.S+tk.E+tk.W
        
    def _component(self):

        self.learnRate_lb = tk.Label(self.__WINDOW, text = '學習率', font = ('Arial', 10))
        self.learnRate_tf = tk.Entry(self.__WINDOW)
        self.learnRate_lb.grid(row = 0)
        self.learnRate_tf.grid(row = 0, column = 1)

        self.endCondition_lb = tk.Label(self.__WINDOW, text = '收斂條件', font = ('Arial', 10))
        self.endCondition_tf = tk.Entry(self.__WINDOW)
        self.endCondition_lb.grid(row = 1)
        self.endCondition_tf.grid(row = 1, column = 1)

        fileOptions = self.getDataSetFile()
        self.fileOptionValue = tk.StringVar()
        self.fileOptionValue.set(fileOptions[0])

        self.fileOption_lb = tk.Label(self.__WINDOW, text = '請選擇檔案', font = ('Arial', 10))
        self.fileOption_op = tk.OptionMenu(self.__WINDOW, self.fileOptionValue, *fileOptions)
        self.fileOption_lb.grid(row = 2)
        self.fileOption_op.grid(row = 2, column = 1)
        # self.fileOption_op['menu'].entryconfigure(1, state = "disabled")

        self.startCalcu_bt = tk.Button(self.__WINDOW, text = "開始", command = self._startCalcu)
        self.startCalcu_bt.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 10, pady = 5)
        
        self.closeWindow_bt = tk.Button(self.__WINDOW, text = "離開", command = self._closeWindow)
        self.closeWindow_bt.grid(row = 0, column = 4, columnspan = 2, rowspan = 2, padx = 10, pady = 5)
        
    def getDataSetFile(self):
        dataFileArr = []
        for dataFile in os.listdir('./dataSet'):
            dataFileArr.append(dataFile)

        return tuple(dataFileArr)

    def checkValueIsFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def _startCalcu(self):
        print(self.fileOptionValue.get())
        if (
            self.checkValueIsFloat(self.learnRate_tf.get()) and 
            self.checkValueIsFloat(self.endCondition_tf.get())
        ):
            print('success')
        else:
            print('fail')

    def _closeWindow(self):
        print('button clicked')
        self.__WINDOW.quit()
        self.__WINDOW.destroy()