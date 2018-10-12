import sys

import tkinter as tk

from src.figure.figurePlt import figurePlt

class UiLayout:

    def __init__(self):
        sys.stdout.write('import from UiLayout in class\n')
        self.__WINDOW = tk.Tk()
        self.__WINDOW.title("Neural Network HW_01")
        self.__WINDOW.resizable(0, 0)
        self.__WINDOW.geometry("750x650+100+100")
        self.__WINDOW.protocol("WM_DELETE_WINDOW", self._closeWindow)
        
        self.__FIGURE_PLT = figurePlt(self.__WINDOW, 2, -2)

        self.__WINDOW.mainloop()
        
    def _closeWindow(self):
        self.__WINDOW.quit()
        self.__WINDOW.destroy()