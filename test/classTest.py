# class Human:
#     def __init__(self,h=0,w=0):
#         self.height=h
#         self.weight=w
#     def BMI(self):
#         return self.weight / ((self.height/100)**2)


import tkinter as tk

class GUI: 
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("My First Tk GUI")
        self.win.resizable(0,0)
        self.win.mainloop()
