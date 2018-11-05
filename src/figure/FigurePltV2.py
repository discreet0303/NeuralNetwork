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
    graph = FigureCanvasTkAgg(self.__FIG, master = self.__WINDOW)
    canvas = graph.get_tk_widget()
    canvas.grid(
      row = 0, 
      column = 0, 
      rowspan = 40, 
      columnspan = 5, 
      sticky='W'
    )
    graph.draw()

    # n = 100

    # for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    #     xs = self.randrange(n, 23, 32)
    #     ys = self.randrange(n, 0, 100)
    #     zs = self.randrange(n, zlow, zhigh)
    #     self.__TEST_PLT.scatter(xs, ys, zs, c=c, marker=m)

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
