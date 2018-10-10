import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

import numpy as np

import matplotlib as mpl
mpl.use("TkAgg")

import matplotlib.pyplot as plt
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def start():
    print('button start')

def close():
    window.quit()
    window.destroy()

def update():
        plt.clf()
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)

        x_number_list2 = [1, 1, 1.5, 1.5]
        y_number_list2 = [0, 1, 0, 1]

        plt.scatter(x_number_list2, y_number_list2, s=10)

        __CANVAS.draw()

def on_exit():
        window.quit()
        window.destroy()

window = tk.Tk()
window.title('Test')
window.resizable(0, 0)
window.protocol("WM_DELETE_WINDOW", on_exit)

startCalcu_bt = tk.Button(
    window, 
    text = "開始", 
    command = start, 
    width = 10
)
startCalcu_bt.grid( row = 0, column = 1 )

close_bt = tk.Button(
    window, 
    text = "close", 
    command = close,
    width = 10
)
close_bt.grid( row = 0, column = 2 )

update_bt = tk.Button(
    window, 
    text = "update", 
    command = update, 
    width = 10
)
update_bt.grid( row = 0, column = 3 )


__FIG = plt.figure()
__CANVAS = FigureCanvasTkAgg(__FIG, master = window)

plt.xlim(-2, 2)
plt.ylim(-2, 2)

x_number_list = [0, 0, 1, 1]
y_number_list = [0, 1, 0, 1]

plt.scatter(x_number_list, y_number_list, s=10)

__CANVAS.draw()
__CANVAS.get_tk_widget().grid(row = 4, column = 0, columnspan = 5, pady = (15, 15), padx = (25, 25))

window.mainloop()

# class Test: 
#     def __init__(self):
#         self.win = tk.Tk()
#         self.win.title("My First Tk GUI")
#         self.win.resizable(0,0)
#         self.win.mainloop()
