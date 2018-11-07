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

  def clearPLT(self):
    self.__TRAINING_PLT.cla()

  def updateFigureLine(self, answer):
    x = np.linspace(-0.1, 1.1)
    y = (answer[0] / answer[2]) - (answer[1] / answer[2]) * x
    self.__TRAINING_PLT.plot(x, y)
    self.__CANVAS.draw()

  def updateFigurePoint(self, data, is2d):
    if is2d:
      for i in data:
        if i[1] == 1:
          color = 'b'
        else:
          color = 'c'
        self.__TRAINING_PLT.scatter(i[0][0], i[0][1], c=color, marker='.')
    else:
      for i in data:
        if i[1] == 1:
          color = 'b'
        else:
          color = 'c'
        self.__TRAINING_PLT.scatter(i[0][0], i[0][1], i[0][2], c=color, marker='.')
    
    self.__CANVAS.draw()

  def figure2dOr3d(self, is2d):
    if not is2d:
      self.__TEST_PLT = self.__FIG.add_subplot(211, projection='3d')
      self.__TEST_PLT.set_title('Test Model')
      self.__TRAINING_PLT = self.__FIG.add_subplot(212, projection='3d')
      self.__TRAINING_PLT.set_title('Training Model')
    else:
      self.__TEST_PLT = self.__FIG.add_subplot(211)
      self.__TEST_PLT.set_title('Test Model')
      self.__TRAINING_PLT = self.__FIG.add_subplot(212)
      self.__TRAINING_PLT.set_title('Training Model')

  def randrange(self, n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
