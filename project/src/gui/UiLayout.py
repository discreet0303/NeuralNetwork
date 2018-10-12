import os
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

import numpy as np

from src.file.File import File
from src.figure.figurePlt import figurePlt
from src.nerual.Perceptron import Perceptron

class UiLayout: 

    def __init__(self):
        self.__WINDOW = tk.Tk()
        self.__WINDOW.title("Neural Network HW_01")
        self.__WINDOW.resizable(0, 0)
        self.__WINDOW.geometry("750x650+100+100")
        self.__WINDOW.protocol("WM_DELETE_WINDOW", self._closeWindow)
        
        self.__FILE = File()

        self._component()

        self.__FIGURE_PLT = figurePlt(self.__WINDOW, 2, -2)

        self.__WINDOW.mainloop()


    def checkValueIsFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _startCalcu(self):
        self.__FIGURE_PLT.clearPlt()
        
        if self.checkValueIsFloat(self.learnRate_tf.get()) or not self.checkValueIsFloat(self.endCondition_tf.get()):
        # if self.checkValueIsFloat(self.learnRate_tf.get()) and self.checkValueIsFloat(self.endCondition_tf.get()):
            self.errorMsg_lb_var.set('')

            fileName = self.fileOptionValue.get()
            data, maxRangeNum, minRangeNum = self.__FILE.getFileContent(fileName, 1)

            __PERCEPTRON = Perceptron(0.1, 100, fileName)
            
            self.showStartW_lb_var.set('起始鍵結值:' + str(__PERCEPTRON.getWeight()) )
            __PERCEPTRON.perceptronCalcu('training')
            testingDataIndex = __PERCEPTRON.getTestingDataIndex()
            arr = __PERCEPTRON.getWeightYToZero()

            self.__FIGURE_PLT.resetDataRagne(maxRangeNum, minRangeNum)
            self.__FIGURE_PLT.updateCanvasForPoint(data, testingDataIndex)
            self.__FIGURE_PLT.updateCanvasForLine(arr)

            self.showEndW_lb_var.set('結束鍵結值:' + str(__PERCEPTRON.getWeight()) )
            self.showTrainingRate_lb_var.set('訓練辨識率:' + str(__PERCEPTRON.getDataSuccessRate('training')) + '%')
            self.showTestingRate_lb_var.set('測試辨識率:' + str(__PERCEPTRON.getDataSuccessRate('testing')) + '%')
           
        else:
            self.errorMsg_lb_var.set('請輸入學習率與收斂條件')



    def _closeWindow(self):
        self.__WINDOW.quit()
        self.__WINDOW.destroy()

    def _component(self):

        self.learnRate_lb = tk.Label(
            self.__WINDOW, 
            text = '學習率', 
            font = ('Arial', 10)
        )
        self.learnRate_lb.grid( row = 0 )

        self.learnRate_tf = tk.Entry(
            self.__WINDOW,
        )
        self.learnRate_tf.grid( row = 0, column = 1 )

        self.endCondition_lb = tk.Label(
            self.__WINDOW, 
            text = '收斂條件', 
            font = ('Arial', 10)
        )
        self.endCondition_lb.grid( row = 1 )

        self.endCondition_tf = tk.Entry(
            self.__WINDOW,
        )
        self.endCondition_tf.grid( row = 1, column = 1 )

        fileOptions = self.__FILE.getDataSetFileName()
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

        self.errorMsg_lb_var = tk.StringVar()
        errorMsg_lb = tk.Label(
            self.__WINDOW,
            textvariable = self.errorMsg_lb_var, 
            font = ('Arial', 10)
        )
        errorMsg_lb.grid( row = 4, columnspan = 2 )

        self.showStartW_lb_var = tk.StringVar()
        self.showStartW_lb_var.set('起始鍵結值:')
        showW_lb = tk.Label(
            self.__WINDOW, 
            textvariable = self.showStartW_lb_var, 
            font = ('Arial', 10)
        )
        showW_lb.grid( row = 6, column = 0 )

        self.showEndW_lb_var = tk.StringVar()
        self.showEndW_lb_var.set('結束鍵結值:')
        showW_lb = tk.Label(
            self.__WINDOW, 
            textvariable = self.showEndW_lb_var, 
            font = ('Arial', 10)
        )
        showW_lb.grid( row = 6, column = 2 )

        self.showTrainingRate_lb_var = tk.StringVar()
        self.showTrainingRate_lb_var.set('訓練辨識率:')
        showTrainingRate_lb = tk.Label(
            self.__WINDOW, 
            textvariable = self.showTrainingRate_lb_var, 
            font = ('Arial', 10)
        )
        showTrainingRate_lb.grid( row = 7, column = 0 )

        self.showTestingRate_lb_var = tk.StringVar()
        self.showTestingRate_lb_var.set('測試辨識率:')
        showTestingRate_lb = tk.Label(
            self.__WINDOW, 
            textvariable = self.showTestingRate_lb_var, 
            font = ('Arial', 10)
        )
        showTestingRate_lb.grid( row = 7, column = 1 )
