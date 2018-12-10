import os, sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import numpy as np
import math
from time import sleep

from src.file.File import File
from src.nerual.Hopfield import Hopfield

class UiLayoutHw3():

	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Neural Network HW_03")
		self.window.resizable(0, 0)

		self.rowNum = 12
		self.colNum = 9

		self.files = File()
		self.fileName = 'Basic'

		self.canvas = tk.Canvas(self.window , width = 450, height = 500)
		self.canvas.grid( row = 0, column = 6, columnspan = 15, rowspan = 20)

		self.componment()
		self.canvasBtComponment(self.rowNum, self.colNum)
		
		self.window.mainloop()
	
	def startTrainData(self):
		self.showText_lb_var.set('開始訓練....')
		data, dataCount = self.files.getHopfieldData(self.fileName + '_Training.txt')
		self.hopfield = Hopfield(data)
		self.showText_lb_var.set('訓練結束')
	
	def startTestData(self):
		if not hasattr(self, 'hopfield'):
			self.showText_lb_var.set('請先點選開始訓練')
		else:
			if self.endCondition_tf.get() == '':
				self.showText_lb_var.set('請輸入最大收斂次數')
			else:
				dataTest, dataTestCount = self.files.getHopfieldData(self.fileName + '_Testing.txt')

				testIndex = int(self.fileOptionValue.get()) - 1
				if self.fileName == 'Basic' and testIndex >= 3:
					testIndex = 2

				inputdata = dataTest[int(testIndex)]
				self.canvas.delete('all')
				self.updateCanvasBtComponment(inputdata)

				sameTimes = 0
				endTimes = int(self.endCondition_tf.get())
				for times in range(endTimes):
					sleep(0.5)
					output = self.hopfield.calcu(inputdata)
					if not np.array_equal(inputdata, output):
						inputdata = output
					
					if sameTimes > 2:
						break
					else:
						sameTimes += 1
					self.canvas.delete('all')
					self.updateCanvasBtComponment(output)

				self.showText_lb_var.set('測試結束')

	def startCustomData(self):
		if not hasattr(self, 'hopfield'):
			self.showText_lb_var.set('請先點選開始訓練')
		else:
			if self.endCondition_tf.get() == '':
				self.showText_lb_var.set('請輸入最大收斂次數')
			else:
				inputdata = []
				for canvasBt in self.canvas.find_withtag("all"):
					color = self.canvas.itemcget(canvasBt, "fill")
					if color == 'white':
						inputdata.append(-1)
					else:
						inputdata.append(1)

				sameTimes = 0
				endTimes = int(self.endCondition_tf.get())
				for times in range(endTimes):
					sleep(0.5)
					output = self.hopfield.calcu(inputdata)
					if not np.array_equal(inputdata, output):
						inputdata = output
					
					if sameTimes > 2:
						break
					else:
						sameTimes += 1
					self.canvas.delete('all')
					self.updateCanvasBtComponment(output)
				self.showText_lb_var.set('測試結束')
	
	def componment(self):
		fileName_lb = tk.Label(
			self.window, 
			text = '請選擇資料集',
			font = ('Arial', 10)
		)
		fileName_lb.grid( row = 0, column = 0, columnspan = 5, padx = 10, sticky = 'W')

		# radiobutton
		self.rb = tk.IntVar()
		self.rb.set(1)

		rb1 = tk.Radiobutton(self.window, text = "Basic", variable = self.rb, value = 1, command = self.sel)
		rb1.grid( row = 1, column = 0, padx = 10)
		rb2 = tk.Radiobutton(self.window, text = "Bonus", variable = self.rb, value = 2, command = self.sel)
		rb2.grid( row = 1, column = 3, padx = 10)

		self.endCondition_lb = tk.Label(
			self.window,
			text = '最大收斂次數',
			font = ('Arial', 10)
		)
		self.endCondition_lb.grid( row = 2, column = 0, columnspan = 3, padx = 10, sticky = "W")

		self.endCondition_tf = tk.Entry(self.window)
		self.endCondition_tf.grid( row = 2, column = 3, columnspan = 3)
		
		self.startTrain_bt = tk.Button(
			self.window, 
			text = "開始訓練", 
			command = self.startTrainData,
			width = 30,
			height = 2,
		)
		self.startTrain_bt.grid(
			row = 3,
			column = 0,
			columnspan = 6,
			padx = 10,
			sticky = 'W'
		)
		fileOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
		self.fileOptionValue = tk.StringVar(self.window)
		self.fileOptionValue.set(fileOptions[0])

		self.fileOption_lb = tk.Label(
			self.window, 
			text = '請選擇測試資料 Index : ', 
			font = ('Arial', 10)
		)
		self.fileOption_lb.grid( row = 4, column = 0, columnspan = 4, padx = 10, sticky = 'W' )

		self.testDataIndex = tk.OptionMenu(
			self.window, 
			self.fileOptionValue,
			*fileOptions
		)
		self.testDataIndex.grid( row = 4, column = 4, columnspan = 2, sticky = 'W' )

		self.startTest_bt = tk.Button(
			self.window, 
			text = "測試資料測試開始", 
			command = self.startTestData,
			width = 30,
			height = 2
		)
		self.startTest_bt.grid(
			row = 5,
			column = 0,
			columnspan = 6,
			padx = 10,
			sticky = 'W'
		)

		self.customTest_bt = tk.Button(
			self.window, 
			text = "自訂資料測試開始", 
			command = self.startCustomData,
			width = 30,
			height = 2
		)
		self.customTest_bt.grid(
			row = 7,
			column = 0,
			columnspan = 6,
			padx = 10,
			sticky = 'W'
		)
		self.showText_lb_var = tk.StringVar()
		self.showText_lb_var.set('...')
		showTestingRate_lb = tk.Label(
			self.window, 
			textvariable = self.showText_lb_var, 
			font = ('Arial', 10)
		)
		showTestingRate_lb.grid( row = 8, column = 0, columnspan = 6, sticky = 'W', padx = 10 )


	def sel(self):
		fileNameArr = ['Basic', 'Bonus']
		self.fileName = fileNameArr[self.rb.get() - 1]
		if self.rb.get() == 1:
			self.rowNum = 12
			self.colNum = 9
		else:
			self.rowNum = 10
			self.colNum = 10

		print(self.fileName)

	def canvasBtComponment(self, rowNum, colNum):
		retLen = 30
		for y in range(rowNum):
			for x in range(colNum):
				leftTopX = 30 + retLen * x + x * 10
				leftTopY = 10 + retLen * y + y * 10
				rightbottomX = leftTopX + retLen
				rightbottomY = leftTopY + retLen
				self.canvasBt = self.canvas.create_rectangle(leftTopX, leftTopY, rightbottomX, rightbottomY, fill="white")

		self.canvas.bind("<Button-1>", self.canvasBtClick)
	
	def canvasBtClick(self, event):
		if self.canvas.find_withtag("current"):
			color = self.canvas.itemcget('current', "fill")
			if color == 'white':
				color = 'black'
			else:
				color = 'white'
				
			self.canvas.itemconfig('current', fill = color)
			self.canvas.after(200)
	
	def updateCanvasBtComponment(self, data):
		retLen = 30
		count = 0
		for y in range(self.rowNum):
			for x in range(self.colNum):
				leftTopX = 30 + retLen * x + x * 10
				leftTopY = 10 + retLen * y + y * 10
				rightbottomX = leftTopX + retLen
				rightbottomY = leftTopY + retLen
				
				if data[count] == -1:
					color = 'white'
				else:
					color = 'black'
				count += 1

				self.canvasBt = self.canvas.create_rectangle(leftTopX, leftTopY, rightbottomX, rightbottomY, fill = color)
		self.canvas.bind("<Button-1>", self.canvasBtClick)
		self.canvas.update()