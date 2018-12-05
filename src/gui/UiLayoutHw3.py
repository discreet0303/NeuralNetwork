import os, sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

from src.file.File import File
from src.nerual.Hopfield import Hopfield

class UiLayoutHw3():

	def __init__(self):
		self.window = tk.Tk()
		self.window.resizable(0, 0)

		self.fileName = 'Basic_Training.txt'
		self.rowNum = 12
		self.colNum = 9

		self.canvas = tk.Canvas(self.window , width = 500, height = 500)
		self.canvas.grid( row = 0, column = 5, columnspan = 15, rowspan = 20)

		self.componment()
		self.canvasBtComponment(self.rowNum, self.colNum)
		
		self.window.mainloop()
	
	def startCalcu(self):
		
		files = File()
		data, dataCount = files.getHopfieldData('Basic_Training.txt')
		dataTest, dataTestCount = files.getHopfieldData('Basic_Testing.txt')
		# data, dataCount = files.getHopfieldData('Bonus_Training.txt')
		# dataTest, dataTestCount = files.getHopfieldData('Bonus_Testing.txt')

		hopfield = Hopfield(data)
		print(data[0])
		test = hopfield.calcu(data[2])

		self.canvas.delete("all")
		self.updateCanvasBtComponment(test)
		# self.canvasBtComponment(10, 8)
	
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
		rb2.grid( row = 2, column = 0, padx = 10)

		self.startTrain_bt = tk.Button(
			self.window, 
			text = "訓練開始", 
			command = self.startCalcu,
			width = 8,
			height = 2,
		)
		self.startTrain_bt.grid(
			row = 3,
			column = 0,
			columnspan = 2,
			padx = 5,
			pady = 5,
		)

		self.startTest_bt = tk.Button(
			self.window, 
			text = "測試開始", 
			command = self.startCalcu,
			width = 8,
			height = 2,
		)
		self.startTest_bt.grid(
			row = 3,
			column = 2,
			columnspan = 2,
			padx = 5,
			pady = 5,
		)

	def sel(self):
		fileNameArr = ['Basic_Training.txt', 'Bonus_Training']
		self.fileName = fileNameArr[self.rb.get() - 1]
		print(self.fileName)


	def canvasBtComponment(self, rowNum, colNum):
		retLen = 30
		for y in range(rowNum):
			for x in range(colNum):
				leftTopX = 30 + retLen * x + x * 10
				leftTopY = 10 + retLen * y + y * 10
				rightbottomX = leftTopX + retLen
				rightbottomY = leftTopY + retLen
				self.canvasBt = self.canvas.create_rectangle(leftTopX, leftTopY, rightbottomX, rightbottomY, fill="black")

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
