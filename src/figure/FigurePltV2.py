import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

class FigurePltV2():
  def __init__(self, __WINDOW):
    self.__WINDOW = __WINDOW
    self.__FIG = Figure(figsize=(4, 8), dpi=96)
    
    self.figure2dOr3d(True)
    self.__COLOR_CODE = ['b', 'g', 'r', 'c', 'm', 'b', 'g', 'r', 'c', 'm']
    self.__FIG.tight_layout()
    self.__CANVAS = FigureCanvasTkAgg(self.__FIG, master = self.__WINDOW)

    self.__CANVAS.get_tk_widget().grid(
      row = 0, 
      column = 0, 
      rowspan = 40, 
      columnspan = 5, 
      sticky='W'
    )
    self.__CANVAS.draw()

  def updateFigureLine(self, answer):
    x = np.linspace(0, 1.1)
    y = (answer[0] / answer[2]) - (answer[1] / answer[2]) * x
    self.__TRAINING_PLT.plot(x, y)
    self.__TRAINING_PLT.set_xlim(0, 1)
    self.__TRAINING_PLT.set_ylim(0, 1)
    self.__CANVAS.draw()

  def updateFigurePoint(self, data, is2d):
    for point in data:
      pos = point[0]
      eVal = point[1]
      color = self.__COLOR_CODE[int(eVal)]
      if is2d:
        self.__TRAINING_PLT.scatter(pos[0], pos[1], c = color, marker = '.')
      else:
        self.__TRAINING_PLT.scatter(pos[0], pos[1], pos[2], c = color, marker = '.')
    # self.__TRAINING_PLT.set_xlim(0, 1)
    # self.__TRAINING_PLT.set_ylim(0, 1)
    self.__CANVAS.draw()

  def updateTestPoint(self, inputData):
    dataLen = len(inputData[0][0]) - 1
    if dataLen == 3:
      self.figure2dOr3d(False)

    for point in inputData:
      pos = point[0]
      eVal = point[1]
      color = self.__COLOR_CODE[int(eVal)]

      if dataLen == 2: 
        self.__TEST_PLT.scatter(pos[1], pos[2], c = color, marker='.')
      elif dataLen == 3: 
        self.__TEST_PLT.scatter(pos[1], pos[2], pos[3], c = color, marker='.')
    self.__CANVAS.draw()

  def clearPlt(self, name):
    if name == 'test':
      self.__TEST_PLT = self.__FIG.add_subplot(211)
      self.__TEST_PLT.cla()
      self.__TEST_PLT.set_title('Original Data')
    elif name == 'train':
      self.__TRAINING_PLT.cla()
      self.__TRAINING_PLT.set_title('The result of the testing data')
      # self.__TRAINING_PLT.set_xlim(0, 1)
      # self.__TRAINING_PLT.set_ylim(0, 1)

  def figure2dOr3d(self, is2d):
    if not is2d:
      self.__TEST_PLT = self.__FIG.add_subplot(211, projection='3d')
    else:
      self.__TEST_PLT = self.__FIG.add_subplot(211)

    self.__TEST_PLT.set_title('Original Data Type')
    self.__TRAINING_PLT = self.__FIG.add_subplot(212)
    self.__TRAINING_PLT.set_title('The result of the testing data')
    # self.__TRAINING_PLT.set_xlim(0, 1)
    # self.__TRAINING_PLT.set_ylim(0, 1)

  def randrange(self, n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
