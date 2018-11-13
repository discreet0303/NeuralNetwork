import os, sys
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter.ttk import *
else:
    import tkinter as tk
    from tkinter import ttk

import random
from src.figure.FigurePltV2 import FigurePltV2
from src.nerual.MultiPerceptron import MultiPerceptron
from src.file.File import File

class UiLayoutV2():
  def __init__(self):
    self.__WINDOW = tk.Tk()
    self.__WINDOW.title("Neural Network HW_02")
    self.__WINDOW.resizable(0, 0)
    self.__WINDOW.geometry("830x775+100+100")
    self.__WINDOW.protocol("WM_DELETE_WINDOW", self._closeWindow)
    
    self.__FIGURE_PLT = FigurePltV2(self.__WINDOW)
    self.__FILE = File()

    self._component()
    self.bitNum25()
    self.__WINDOW.mainloop()

  def startCalcu(self):
    # setting learnRate endTime
    # learnRate = self.learnRate_tf.get()
    # endTime = self.endCondition_tf.get()

    fileName = self.fileOptionValue.get()
    inputData, eValList = self.__FILE.getFileContentV2(fileName)
    # print(inputData)
    self.__FIGURE_PLT.clearPlt('test')
    self.__FIGURE_PLT.updateTestPoint(inputData)
    self.trainingWeight_tv.delete(*self.trainingWeight_tv.get_children())

    a = MultiPerceptron(self.__FIGURE_PLT)
    testingData, trainingData = self.randomDataTo2Array(inputData)
    data, weight = a.startTraining(inputData, eValList)
    # data, weight = a.startTraining(testingData, eValList)
    self.__FIGURE_PLT.clearPlt('train')
    self.__FIGURE_PLT.updateFigurePoint(data, True)
    # self.__FIGURE_PLT.updateFigureLine(weight)

    testCorrectRate = a.getDataCorrectRate(testingData)
    testCorrectRate = testCorrectRate / len(testingData) * 100
    self.showTestingRate_lb_var.set('測試辨識率: ' + str(testCorrectRate) + '%')

    trainCorrectRate = a.getDataCorrectRate(trainingData)
    trainCorrectRate = trainCorrectRate / len(trainingData) * 100
    self.showTrainingRate_lb_var.set('訓練辨識率: ' + str(trainCorrectRate) + '%')

    rmse = a.getRMSE()
    rmse = rmse / len(inputData)
    self.showRMSERate_lb_var.set('RMSE: ' + str(rmse))

    allWeight = a.getAllModelWeight()

    self.updateWeightData('(Level, Index) : weight')
    for levelIndex, level in enumerate(allWeight):
      for itemIndex, item in enumerate(level):
        level = '(' + str(levelIndex) + ',' + str(itemIndex) + ')   :  '
        temp = level + '[' + str(round(item[0], 3)) + ',' + str(round(item[1], 3)) + ',' + str(round(item[1], 3)) + ']'
        self.updateWeightData(temp)

  def startCalcuForBitNumTesting(self):
    testData = self.getCheckboxVal()
    print(self.__NUM_PERCEPTRON.getFinalOutpuToRegex(testData))

  def startCalcuForBitNumTraining(self):
    inputData, eValList = self.__FILE.getFileContentV2('Number.txt')
    self.__NUM_PERCEPTRON  = MultiPerceptron(self.__FIGURE_PLT)
    data, weight = self.__NUM_PERCEPTRON.startTraining(inputData, eValList)

  def randomDataTo2Array(self, data):
    if len(data) < 10:
      return data, data
    index = 0
    testingCount = int((len(data) / 3) * 1)
    dataForTraining = data[:]
    dataForTesting = []
    while testingCount != len(dataForTesting):
      trainingRange = len(dataForTraining) - 1
      index = random.randint(0, trainingRange)
      dataForTesting.append(dataForTraining[index])
      del dataForTraining[index]

    return dataForTraining, dataForTesting

  def _component(self):
    self.learnRate_lb = tk.Label(
      self.__WINDOW, 
      text = '學習率', 
      font = ('Arial', 10)
    )
    self.learnRate_lb.grid( row = 0, column = 6, columnspan = 3, sticky = "E")

    self.learnRate_tf = tk.Entry(
      self.__WINDOW,
    )
    self.learnRate_tf.grid( row = 0, column = 9, columnspan = 5)

    self.endCondition_lb = tk.Label(
      self.__WINDOW, 
      text = '收斂條件(次數)', 
      font = ('Arial', 10)
    )
    self.endCondition_lb.grid( row = 1, column = 6, columnspan = 3, sticky = "E")

    self.endCondition_tf = tk.Entry(
      self.__WINDOW,
    )
    self.endCondition_tf.grid( row = 1, column = 9, columnspan = 5 )

    self.startCalcu_bt = tk.Button(
      self.__WINDOW, 
      text = "開始", 
      command = self.startCalcu, 
      width = 5,
      height = 3,
    )
    self.startCalcu_bt.grid(
      row = 0,
      column = 14,
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
      column = 16,
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
    self.fileOption_lb.grid( row = 2, column = 6, columnspan = 3 )

    self.fileOption_op = tk.OptionMenu(
        self.__WINDOW, 
        self.fileOptionValue,
        *fileOptions
    )
    self.fileOption_op.grid( row = 2, column = 9, columnspan = 5 )

    self.showTestingRate_lb_var = tk.StringVar()
    self.showTestingRate_lb_var.set('測試辨識率: 無')
    showTestingRate_lb = tk.Label(
        self.__WINDOW, 
        textvariable = self.showTestingRate_lb_var, 
        font = ('Arial', 10)
    )
    showTestingRate_lb.grid( row = 4, column = 6, columnspan = 10, sticky = 'W', padx = 10 )

    self.showTrainingRate_lb_var = tk.StringVar()
    self.showTrainingRate_lb_var.set('訓練辨識率: 無')
    showTrainingRate_lb = tk.Label(
        self.__WINDOW, 
        textvariable = self.showTrainingRate_lb_var, 
        font = ('Arial', 10)
    )
    showTrainingRate_lb.grid( row = 5, column = 6, columnspan = 10, sticky = 'W', padx = 10 )

    self.showRMSERate_lb_var = tk.StringVar()
    self.showRMSERate_lb_var.set('RMSE: 無')
    showRMSERate_lb = tk.Label(
        self.__WINDOW, 
        textvariable = self.showRMSERate_lb_var, 
        font = ('Arial', 10)
    )
    showRMSERate_lb.grid( row = 6, column = 6, columnspan = 10, sticky = 'W', padx = 10 )
    
    allweight_lb = tk.Label(
      self.__WINDOW, 
      text = "所有感知機鍵結值", 
    )
    allweight_lb.grid( row = 7, column = 7, padx = 20 )

    self.trainingWeight_tv = ttk.Treeview(self.__WINDOW)
    self.trainingWeight_tv.column("#0", anchor="w", width = 400)
    self.trainingWeight_tv.grid( 
      row = 8,
      column = 6,
      rowspan = 15,
      columnspan = 25,
      padx = 20,
    )

  def updateWeightData(self, datas):
    self.trainingWeight_tv.insert('', 'end', text = datas)

  def _closeWindow(self):
    self.__WINDOW.quit()
    self.__WINDOW.destroy()

  def getCheckboxVal(self):
    temp = []
    # 0
    temp.append(self.var00.get())
    temp.append(self.var01.get())
    temp.append(self.var02.get())
    temp.append(self.var03.get())
    temp.append(self.var04.get())
    # 1
    temp.append(self.var10.get())
    temp.append(self.var11.get())
    temp.append(self.var12.get())
    temp.append(self.var13.get())
    temp.append(self.var14.get())
    # 2
    temp.append(self.var20.get())
    temp.append(self.var21.get())
    temp.append(self.var22.get())
    temp.append(self.var23.get())
    temp.append(self.var24.get())
    # 3
    temp.append(self.var30.get())
    temp.append(self.var31.get())
    temp.append(self.var32.get())
    temp.append(self.var33.get())
    temp.append(self.var34.get())
    # 4
    temp.append(self.var40.get())
    temp.append(self.var41.get())
    temp.append(self.var42.get())
    temp.append(self.var43.get())
    temp.append(self.var44.get())

    return temp

  def bitNum25(self):
    bitNum_lb = tk.Label(
      self.__WINDOW, 
      text = "數字辨識", 
    )
    bitNum_lb.grid(
      row = 26,
      column = 7
    )

    self.startCalcuForBitNumTraining_bt = tk.Button(
      self.__WINDOW, 
      text = "訓練開始", 
      command = self.startCalcuForBitNumTraining, 
      width = 9,
      height = 3,
    )
    self.startCalcuForBitNumTraining_bt.grid(
      row = 27,
      column = 6,
      rowspan = 2,
      columnspan = 3,
      padx = 5,
      pady = 5,
    )

    self.startCalcuForBitNumTesting_bt = tk.Button(
      self.__WINDOW, 
      text = "測試", 
      command = self.startCalcuForBitNumTesting, 
      width = 9,
      height = 3,
    )
    self.startCalcuForBitNumTesting_bt.grid(
      row = 29,
      column = 6,
      rowspan = 2,
      columnspan = 3,
      padx = 5,
      pady = 5,
    )

    startRow = 27
    startColumn = 10
    # 0
    self.var00 = tk.IntVar()
    self.bitNum00_cb = tk.Checkbutton(self.__WINDOW, variable = self.var00)
    self.bitNum00_cb.grid(row = startRow, column = startColumn)
    self.var01 = tk.IntVar()
    self.bitNum01_cb = tk.Checkbutton(self.__WINDOW, variable = self.var01)
    self.bitNum01_cb.grid(row = startRow, column = startColumn + 1)
    self.var02= tk.IntVar()
    self.bitNum02_cb = tk.Checkbutton(self.__WINDOW, variable = self.var02)
    self.bitNum02_cb.grid(row = startRow, column = startColumn + 2)
    self.var03 = tk.IntVar()
    self.bitNum03_cb = tk.Checkbutton(self.__WINDOW, variable = self.var03)
    self.bitNum03_cb.grid(row = startRow, column = startColumn + 3)
    self.var04 = tk.IntVar()
    self.bitNum04_cb = tk.Checkbutton(self.__WINDOW, variable = self.var04)
    self.bitNum04_cb.grid(row = startRow, column = startColumn + 4)
    # 1
    self.var10 = tk.IntVar()
    self.bitNum00_cb = tk.Checkbutton(self.__WINDOW, variable = self.var10)
    self.bitNum00_cb.grid(row = startRow + 1, column = startColumn)
    self.var11 = tk.IntVar()
    self.bitNum01_cb = tk.Checkbutton(self.__WINDOW, variable = self.var11)
    self.bitNum01_cb.grid(row = startRow + 1, column = startColumn + 1)
    self.var12= tk.IntVar()
    self.bitNum02_cb = tk.Checkbutton(self.__WINDOW, variable = self.var12)
    self.bitNum02_cb.grid(row = startRow + 1, column = startColumn + 2)
    self.var13 = tk.IntVar()
    self.bitNum03_cb = tk.Checkbutton(self.__WINDOW, variable = self.var13)
    self.bitNum03_cb.grid(row = startRow + 1, column = startColumn + 3)
    self.var14 = tk.IntVar()
    self.bitNum04_cb = tk.Checkbutton(self.__WINDOW, variable = self.var14)
    self.bitNum04_cb.grid(row = startRow + 1, column = startColumn + 4)
    # 2
    self.var20 = tk.IntVar()
    self.bitNum00_cb = tk.Checkbutton(self.__WINDOW, variable = self.var20)
    self.bitNum00_cb.grid(row = startRow + 2, column = startColumn)
    self.var21 = tk.IntVar()
    self.bitNum01_cb = tk.Checkbutton(self.__WINDOW, variable = self.var21)
    self.bitNum01_cb.grid(row = startRow + 2, column = startColumn + 1)
    self.var22= tk.IntVar()
    self.bitNum02_cb = tk.Checkbutton(self.__WINDOW, variable = self.var22)
    self.bitNum02_cb.grid(row = startRow + 2, column = startColumn + 2)
    self.var23 = tk.IntVar()
    self.bitNum03_cb = tk.Checkbutton(self.__WINDOW, variable = self.var23)
    self.bitNum03_cb.grid(row = startRow + 2, column = startColumn + 3)
    self.var24 = tk.IntVar()
    self.bitNum04_cb = tk.Checkbutton(self.__WINDOW, variable = self.var24)
    self.bitNum04_cb.grid(row = startRow + 2, column = startColumn + 4)
    # 3
    self.var30 = tk.IntVar()
    self.bitNum00_cb = tk.Checkbutton(self.__WINDOW, variable = self.var30)
    self.bitNum00_cb.grid(row = startRow + 3, column = startColumn)
    self.var31 = tk.IntVar()
    self.bitNum01_cb = tk.Checkbutton(self.__WINDOW, variable = self.var31)
    self.bitNum01_cb.grid(row = startRow + 3, column = startColumn + 1)
    self.var32= tk.IntVar()
    self.bitNum02_cb = tk.Checkbutton(self.__WINDOW, variable = self.var32)
    self.bitNum02_cb.grid(row = startRow + 3, column = startColumn + 2)
    self.var33 = tk.IntVar()
    self.bitNum03_cb = tk.Checkbutton(self.__WINDOW, variable = self.var33)
    self.bitNum03_cb.grid(row = startRow + 3, column = startColumn + 3)
    self.var34 = tk.IntVar()
    self.bitNum04_cb = tk.Checkbutton(self.__WINDOW, variable = self.var34)
    self.bitNum04_cb.grid(row = startRow + 3, column = startColumn + 4)
    # 4
    self.var40 = tk.IntVar()
    self.bitNum00_cb = tk.Checkbutton(self.__WINDOW, variable = self.var40)
    self.bitNum00_cb.grid(row = startRow + 4, column = startColumn)
    self.var41 = tk.IntVar()
    self.bitNum01_cb = tk.Checkbutton(self.__WINDOW, variable = self.var41)
    self.bitNum01_cb.grid(row = startRow + 4, column = startColumn + 1)
    self.var42= tk.IntVar()
    self.bitNum02_cb = tk.Checkbutton(self.__WINDOW, variable = self.var42)
    self.bitNum02_cb.grid(row = startRow + 4, column = startColumn + 2)
    self.var43 = tk.IntVar()
    self.bitNum03_cb = tk.Checkbutton(self.__WINDOW, variable = self.var43)
    self.bitNum03_cb.grid(row = startRow + 4, column = startColumn + 3)
    self.var44 = tk.IntVar()
    self.bitNum04_cb = tk.Checkbutton(self.__WINDOW, variable = self.var44)
    self.bitNum04_cb.grid(row = startRow + 4, column = startColumn + 4)
