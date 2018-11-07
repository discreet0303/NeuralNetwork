from src.nerual.MultiPerceptronItem import MultiPerceptronItem

import numpy as np
import math
class MultiPerceptron():

  def __init__(self):
    print('MultiPerceptron')
    self.__LEVEL = 2
    self.__ITEM = 2

    self.__ERROR = 0

    self.__PERCEPTRON_MODEL = []
    for level in range(0, self.__LEVEL - 1):
      temp = []
      for item in range(0, self.__ITEM):
        temp.append(MultiPerceptronItem())
      self.__PERCEPTRON_MODEL.append(temp)
    self.__PERCEPTRON_MODEL.append([MultiPerceptronItem()])

    # self.__PERCEPTRON_MODEL[0][0].setWeight([-1.198, 0.912, 1.179])
    # self.__PERCEPTRON_MODEL[0][1].setWeight([0.294, 0.826, 0.98])
    # self.__PERCEPTRON_MODEL[1][0].setWeight([0.216, 0.384, -0.189])
    self.__PERCEPTRON_MODEL[0][0].setWeight([-1.2, 1, 1])
    self.__PERCEPTRON_MODEL[0][1].setWeight([0.3, 1, 1])
    self.__PERCEPTRON_MODEL[1][0].setWeight([0.5, 0.4, 0.8])

  def sig(self, data, w):
      expNum = np.dot(data, w)
      sigmoidalNum = round( 1 / (1 + math.exp(-1 * expNum)), 3 )
      # print(sigmoidalNum)
  
  def startTraining(self):
    xor = [
      [[-1, 0, 0], 0],
      [[-1, 0, 1], 1],
      [[-1, 1, 0], 1],
      [[-1, 1, 1], 0],
    ]

    for i in range(800):
      for data in xor:
        self.singleDataTraining(data)
        
    data1 = []
    # w = []
    w = [
      # [-1.198, 0.912, 1.179],
      # [0.294, 0.826, 0.98],
      # [0.216, 0.384, -0.189],

      # [-1.2, 0.898, 0.999],
      # [0.183, 0.728, 1.1],
      # [0.208, 0.233, 0.004],
      [-0.743, 1.4, 1.348],
      [1.084, 0.822, 0.766],
      [0.368, 0.931, -1.068],
    ]
    for i in xor:
      # x = self.calcu(i[0], self.__PERCEPTRON_MODEL[0][0].getWeight())
      # y = self.calcu(i[0], self.__PERCEPTRON_MODEL[0][1].getWeight())
      x = self.calcu(i[0], w[0])
      y = self.calcu(i[0], w[1])
      data1.append([[x, y],i[1]])
    return data1, w[2]
    return data1, self.__PERCEPTRON_MODEL[0][1].getWeight()

  def singleDataTraining(self, inputData):
    print('inputData: ', inputData)
    print('start weight w1: ', self.__PERCEPTRON_MODEL[0][0].getWeight())
    print('start weight w2: ', self.__PERCEPTRON_MODEL[0][1].getWeight())
    print('start weight w3: ', self.__PERCEPTRON_MODEL[1][0].getWeight())
    for levelCount, level in enumerate(self.__PERCEPTRON_MODEL):
      for perceptron in level:
        if levelCount == 0:
          perceptron.setInputData(inputData)
        else:
          eOutput = self.getLevelPerceptronOutput(self.__PERCEPTRON_MODEL[levelCount - 1])
          perceptron.setInputData([eOutput, inputData[1]])
          # print('eoutput')
          # print(eOutput)
    
    print('output w1: ', self.__PERCEPTRON_MODEL[0][0].getEOutput())
    print('output w2: ', self.__PERCEPTRON_MODEL[0][1].getEOutput())
    print('output w3: ', self.__PERCEPTRON_MODEL[1][0].getEOutput())
    # self.sig(
    #   [-1, self.__PERCEPTRON_MODEL[0][0].getEOutput(),
    #   self.__PERCEPTRON_MODEL[0][1].getEOutput()], self.__PERCEPTRON_MODEL[1][0].getWeight())


    finalOutput = self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput()
    self.__ERROR = self.__ERROR + 0.5 * (inputData[1] - finalOutput) ** 2

    if not self.checkWeight(inputData[1], finalOutput):
      print('changing Weight')
      last = 0
      weight = self.__PERCEPTRON_MODEL[1][0].getWeight()
      for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL[::-1]):
        for backPerceptronIndex, backPerceptron in enumerate(level):
          if levelIndex == 0:
            # regexE = self.regexEValue()
            # middleVal = regexE[inputData[1]]['middleVal']
            if inputData[1] == 0:
              backPerceptron.setBackPropagate(True, 0, 0)
            else:
              backPerceptron.setBackPropagate(True, 0, 1)
            last = backPerceptron.getBackPropagate()
          else:
            # weight = self.__PERCEPTRON_MODEL[1][0].getWeight()
            print('backPerceptronIndex:', backPerceptronIndex)
            print(backPerceptron.getEOutput())
            print(last)
            print(weight[backPerceptronIndex + 1])
            backPerceptron.setBackPropagate(False, last, weight[backPerceptronIndex + 1])
            # if backPerceptronIndex == 0:
            #   backPerceptron.setBackPropagate(False, last, 0.4)
            # elif backPerceptronIndex == 1:
            #   backPerceptron.setBackPropagate(False, last, 0.8)
          backPerceptron.updateWeight()
      
    print('end weight w1: ', self.__PERCEPTRON_MODEL[0][0].getWeight())
    print('end weight w2: ', self.__PERCEPTRON_MODEL[0][1].getWeight())
    print('end weight w3: ', self.__PERCEPTRON_MODEL[1][0].getWeight())
    print("W1 BackPropagate: ", self.__PERCEPTRON_MODEL[0][0].getBackPropagate())
    print("W2 BackPropagate: ", self.__PERCEPTRON_MODEL[0][1].getBackPropagate())
    print("W3 BackPropagate: ", self.__PERCEPTRON_MODEL[1][0].getBackPropagate())
    print('======================================================================')
      # print(self.__ERROR)
      # print(inputData)
    #   return True
    # return False
    
    # finalOutput1 = self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0]
    # self.__ERROR = self.__ERROR + 0.5 * (inputData[1] - finalOutput1.getEOutput()) ** 2

  def getLevelPerceptronOutput(self, perceptronItems):
    eLevelOutputData = [-1]
    for item in perceptronItems:
      eLevelOutputData.append(item.getEOutput())
    return eLevelOutputData

  def checkWeight(self, eValue, eOutput):
    regexE = self.regexEValue()
    minRange = regexE[eValue]['minRange']
    maxRange = regexE[eValue]['maxRange']
    if minRange < eOutput <= maxRange:
        return True
    else:
        return False

  def regexEValue(self):
    allEValue = [0, 1]
    temp = {}
    num = 1 / len(allEValue)
    for index, value in enumerate(allEValue):
        temp.update({
            value: {
                'e': value,
                'middleVal': (index + 0.5) * num ,
                'minRange': index * num,
                'maxRange': (index + 1) * num
            }
        })
    return temp

  def calcu(self, inputData, weight):
    temp1 = inputData[1] * weight[1]
    temp2 = inputData[2] * weight[2]
    expNum = temp1 + temp2 - weight[0]
    sigmoidalNum = 1 / (1 + math.exp(-1 * expNum))
    return sigmoidalNum

  def printWeight(self):
    for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL):
      print('------')
      for itemIndex, item in enumerate(level):
        print('level:', levelIndex, 'weight:', itemIndex)
        print(item.getWeight())
    print(self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput())