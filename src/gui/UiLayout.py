import tkinter as tk
import os

import numpy as np

from src.file.File import File
from src.figure.figurePlt import figurePlt

class UiLayout: 

    def __init__(self):
        self.__WINDOW = tk.Tk()
        self.__WINDOW.title("Neural Network HW_01")
        self.__WINDOW.resizable(0, 0)
        self.__WINDOW.geometry("1000x700+500+300")
        
        self.__FILE = File()

        self._component()
        figurePlt(self.__WINDOW)

        self.__WINDOW.mainloop()

    def _component(self):

        self.learnRate_lb = tk.Label(
            self.__WINDOW, 
            text = '學習率', 
            font = ('Arial', 10)
        )
        self.learnRate_lb.grid( row = 0 )

        self.learnRate_tf = tk.Entry(
            self.__WINDOW
        )
        self.learnRate_tf.grid( row = 0, column = 1 )

        self.endCondition_lb = tk.Label(
            self.__WINDOW, 
            text = '收斂條件', 
            font = ('Arial', 10)
        )
        self.endCondition_lb.grid( row = 1 )

        self.endCondition_tf = tk.Entry(
            self.__WINDOW
        )
        self.endCondition_tf.grid( row = 1, column = 1 )

        fileOptions = self.__FILE.getDataSetFile()
        self.fileOptionValue = tk.StringVar(self.__WINDOW)
        self.fileOptionValue.set(fileOptions[0])

        self.fileOption_lb = tk.Label(
            self.__WINDOW, 
            text = '請選擇檔案', 
            font = ('Arial', 10)
        )
        self.fileOption_lb.grid( row = 2 )

        self.fileOption_op = tk.OptionMenu(
            self.__WINDOW, 
            self.fileOptionValue, 
            *fileOptions
        )
        self.fileOption_op.grid( row = 2, column = 1 )

        self.startCalcu_bt = tk.Button(
            self.__WINDOW, 
            text = "開始", 
            command = self._startCalcu, 
            width = 10
        )
        self.startCalcu_bt.grid(
            row = 0, 
            rowspan = 2, 
            column = 2, 
            columnspan = 2, 
            padx = 10, 
            pady = 5
        )
        
        self.closeWindow_bt = tk.Button(
            self.__WINDOW, 
            text = "離開", 
            command = self._closeWindow, 
            width = 10
        )
        self.closeWindow_bt.grid(
            row = 0, 
            column = 4, 
            columnspan = 2, 
            rowspan = 2, 
            padx = 10, 
            pady = 5
        )
        

    def checkValueIsFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _startCalcu(self):
        
        self.__FILE.getFileContent(self.fileOptionValue.get())
        self.__FILE.sortFileContentWithIndex(self.fileOptionValue.get())
        if self.checkValueIsFloat(self.learnRate_tf.get()) and self.checkValueIsFloat(self.endCondition_tf.get()):

            self.__WINDOW.quit()
            self.__WINDOW.destroy()
            print('success')
        else:
            print('fail')

    def _closeWindow(self):
        print('button clicked')
        self.__WINDOW.quit()
        self.__WINDOW.destroy()