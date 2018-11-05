import os, sys
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter.ttk import *
else:
    import tkinter as tk
    from tkinter import ttk

from src.figure.figurePlt import figurePlt
from src.figure.FigurePltV2 import FigurePltV2

class UiLayoutV2():
  def __init__(self):
    self.__WINDOW = tk.Tk()
    self.__WINDOW.title("Neural Network HW_02")
    self.__WINDOW.resizable(0, 0)
    self.__WINDOW.geometry("800x800+100+100")
    self.__WINDOW.protocol("WM_DELETE_WINDOW", self._closeWindow)
    
    self.__FIGURE_PLT = FigurePltV2(self.__WINDOW)
    
    self._component()
    self.tableLayout()
    
    self.__WINDOW.mainloop()

  def _startCalcu(self):
    print('_startCalcu')

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
      command = self._startCalcu, 
      width = 10
    )
    self.startCalcu_bt.grid(
      row = 2, 
      column = 6,
      pady = 5,
    )

    self.closeWindow_bt = tk.Button(
      self.__WINDOW, 
      text = "結束", 
      command = self._closeWindow, 
      width = 10
    )
    self.closeWindow_bt.grid(
      row = 2,
      column = 7,
      pady = 5,
    )

  def tableLayout(self):
    tv = ttk.Treeview(self.__WINDOW)
    tv['columns'] = ('Value')
    tv.heading("#0", text='WeightIndex', anchor='w')
    tv.column("#0", anchor="w", width = 75)
    tv.heading('Value', text='Value')
    tv.column('Value', anchor='center', width = 200)
    tv.grid( 
      row = 20, 
      column = 6,
      rowspan = 10,
      columnspan = 10
    )
    tv.insert('', 'end', text="1", values=('10:00'))
    tv.insert('', 'end', text="2", values=('10:00'))
    tv.insert('', 'end', text="3", values=('10:00'))
    tv.insert('', 'end', text="4", values=('10:00'))
    tv.insert('', 'end', text="5", values=('10:00'))
    tv.insert('', 'end', text="6", values=('10:00'))
    tv.insert('', 'end', text="7", values=('10:00'))

  def _closeWindow(self):
    self.__WINDOW.quit()
    self.__WINDOW.destroy()
