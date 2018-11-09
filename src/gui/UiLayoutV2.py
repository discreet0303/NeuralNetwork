import os, sys
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter.ttk import *
else:
    import tkinter as tk
    from tkinter import ttk

from src.figure.FigurePltV2 import FigurePltV2
from src.nerual.MultiPerceptron import MultiPerceptron
from src.file.File import File

class UiLayoutV2():
  def __init__(self):
    self.__WINDOW = tk.Tk()
    self.__WINDOW.title("Neural Network HW_02")
    self.__WINDOW.resizable(0, 0)
    self.__WINDOW.geometry("740x775+100+100")
    self.__WINDOW.protocol("WM_DELETE_WINDOW", self._closeWindow)
    
    self.__FIGURE_PLT = FigurePltV2(self.__WINDOW)
    self.__FILE = File()
    self._component()
    
    self.__WINDOW.mainloop()

  def startCalcu(self):
    # setting learnRate endTime
    # learnRate = self.learnRate_tf.get()
    # endTime = self.endCondition_tf.get()

    fileName = self.fileOptionValue.get()
    inputData, eValList = self.__FILE.getFileContentV2(fileName)
    
    self.__FIGURE_PLT.clearPlt('test')
    self.__FIGURE_PLT.updateTestPoint(inputData)

    a = MultiPerceptron()
    data, weight = a.startTraining(inputData, eValList)
    self.__FIGURE_PLT.clearPlt('train')
    self.__FIGURE_PLT.updateFigurePoint(data, True)
    self.__FIGURE_PLT.updateFigureLine(weight)
    print('startCalcu')

  def _component(self):
    self.learnRate_lb = tk.Label(
      self.__WINDOW, 
      text = '學習率', 
      font = ('Arial', 10)
    )
    self.learnRate_lb.grid( row = 0, column = 6, sticky = "E")

    self.learnRate_tf = tk.Entry(
      self.__WINDOW,
    )
    self.learnRate_tf.grid( row = 0, column = 7)

    self.endCondition_lb = tk.Label(
      self.__WINDOW, 
      text = '收斂條件(次數)', 
      font = ('Arial', 10)
    )
    self.endCondition_lb.grid( row = 1, column = 6, sticky = "E")

    self.endCondition_tf = tk.Entry(
      self.__WINDOW,
    )
    self.endCondition_tf.grid( row = 1, column = 7 )

    self.startCalcu_bt = tk.Button(
      self.__WINDOW, 
      text = "開始", 
      command = self.startCalcu, 
      width = 5,
      height = 3,
    )
    self.startCalcu_bt.grid(
      row = 0,
      column = 8,
      rowspan = 2,
      padx = 5,
      pady = 5,
    )

    self.closeWindow_bt = tk.Button(
      self.__WINDOW, 
      text = "結束", 
      command = self._closeWindow, 
      width = 5,
      height = 3,
    )
    self.closeWindow_bt.grid(
      row = 0,
      column = 9,
      rowspan = 2,
      padx = 5,
      pady = 5,
    )

    fileOptions = self.__FILE.getDataSetFileName()
    self.fileOptionValue = tk.StringVar(self.__WINDOW)
    self.fileOptionValue.set(fileOptions[0])

    self.fileOption_lb = tk.Label(
        self.__WINDOW, 
        text = '請選擇檔案', 
        font = ('Arial', 10)
    )
    self.fileOption_lb.grid( row = 2, column = 6 )

    self.fileOption_op = tk.OptionMenu(
        self.__WINDOW, 
        self.fileOptionValue,
        *fileOptions
    )
    self.fileOption_op.grid( row = 2, column = 7 )

    self.testWeight_lb = tk.Label(
      self.__WINDOW, 
      text = '訓練前 Weight', 
      font = ('Arial', 10)
    )
    self.testWeight_lb.grid( row = 18, column = 7)

    self.testgWeight_tv = ttk.Treeview(self.__WINDOW)
    self.testgWeight_tv['columns'] = ('Value')
    self.testgWeight_tv.heading("#0", text='WeightIndex', anchor='w')
    self.testgWeight_tv.column("#0", anchor="w", width = 100)
    self.testgWeight_tv.heading('Value', text='Value')
    self.testgWeight_tv.column('Value', anchor='center', width = 200)
    self.testgWeight_tv.grid( 
      row = 19, 
      column = 6,
      rowspan = 10,
      columnspan = 5,
      padx = 20,
    )
    self.trainingWeight_lb = tk.Label(
      self.__WINDOW, 
      text = '訓練後 Weight', 
      font = ('Arial', 10)
    )
    self.trainingWeight_lb.grid( row = 29, column = 7)

    self.trainingWeight_tv = ttk.Treeview(self.__WINDOW)
    self.trainingWeight_tv['columns'] = ('Value')
    self.trainingWeight_tv.heading("#0", text='WeightIndex', anchor='w')
    self.trainingWeight_tv.column("#0", anchor="w", width = 100)
    self.trainingWeight_tv.heading('Value', text='Value')
    self.trainingWeight_tv.column('Value', anchor='center', width = 200)
    self.trainingWeight_tv.grid( 
      row = 30, 
      column = 6,
      rowspan = 10,
      columnspan = 5,
      padx = 20,
    )

  def updateWeightData(self, tv, datas):
    for index, data in enumerate(datas):
      tv.insert('', 'end', text = index, values=('0.12345789123456'))

  def _closeWindow(self):
    self.__WINDOW.quit()
    self.__WINDOW.destroy()
