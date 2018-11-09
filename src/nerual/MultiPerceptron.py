from src.nerual.MultiPerceptronItem import MultiPerceptronItem

import numpy as np
import math
class MultiPerceptron():

  def __init__(self):
    print('MultiPerceptron')
    self.__LEVEL = 3
    self.__ITEM = 2

    self.__ERROR = 0

    self.__PERCEPTRON_MODEL = [
      [MultiPerceptronItem(), MultiPerceptronItem(), MultiPerceptronItem()],
      [MultiPerceptronItem(), MultiPerceptronItem()],
      [MultiPerceptronItem()],
    ]
    # for level in range(0, self.__LEVEL - 1):
    #   temp = []
    #   for item in range(0, self.__ITEM):
    #     temp.append(MultiPerceptronItem())
    #   self.__PERCEPTRON_MODEL.append(temp)
    # self.__PERCEPTRON_MODEL.append([MultiPerceptronItem()])

  def startTraining(self, inputData, eValList):
    xor = inputData
    self.setRegexEValue(eValList)
    # self.setRegexEValue([0, 1])
    # xor = [
    #   [[-1, 0, 0], 0],
    #   [[-1, 0, 1], 1],
    #   [[-1, 1, 0], 1],
    #   [[-1, 1, 1], 0],
    # ]
    # xor = [
    #   [[-1, 1, 1], 0],
    #   [[-1, 1, 0], 0],
    #   [[-1, 0, 0], 1],
    #   [[-1, 0, 1], 1],
    # ]

    for i in range(500):
      for data in xor:
        self.singleDataTraining(data)
        
    data1 = []
    # w = [
    #   [-1.198, 0.912, 1.179],
    #   [0.294, 0.826, 0.98],
    #   [0.216, 0.384, -0.189],
    # ]
    for i in xor:
      x = self.calcu(i[0], self.__PERCEPTRON_MODEL[0][0].getWeight())
      y = self.calcu(i[0], self.__PERCEPTRON_MODEL[0][1].getWeight())
      # x = self.calcu(i[0], w[0])
      # y = self.calcu(i[0], w[1])
      data1.append([[x, y],i[1]])
    # print(self.__PERCEPTRON_MODEL[0][0].getWeight())
    # print(self.__PERCEPTRON_MODEL[0][1].getWeight())
    # print(self.__PERCEPTRON_MODEL[1][0].getWeight())

    self.printWeight()

    # return data1, w[2]
    return data1, self.__PERCEPTRON_MODEL[1][0].getWeight()

  def singleDataTraining(self, inputData):
    for levelCount, level in enumerate(self.__PERCEPTRON_MODEL):
      for perceptron in level:
        if levelCount == 0:
          perceptron.setInputData(inputData)
        else:
          eOutput = self.getLevelPerceptronOutput(self.__PERCEPTRON_MODEL[levelCount - 1])
          perceptron.setInputData([eOutput, inputData[1]])

    finalOutput = self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput()
    self.__ERROR = self.__ERROR + 0.5 * (inputData[1] - finalOutput) ** 2

    if not self.checkWeight(inputData[1], finalOutput):
      last = 0
      weight = self.__PERCEPTRON_MODEL[1][0].getWeight()
      for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL[::-1]):
        for backPerceptronIndex, backPerceptron in enumerate(level):
          if levelIndex == 0:
            regexE = self.getRegexEValue()
            middleVal = regexE[inputData[1]]['middleVal']
            # if inputData[1] == 0:
            #   backPerceptron.setBackPropagate(True, 0, 0)
            # else:
            #   backPerceptron.setBackPropagate(True, 0, 1)
            backPerceptron.setBackPropagate(True, 0, middleVal)
            last = backPerceptron.getBackPropagate()
          else:
            # weight = self.__PERCEPTRON_MODEL[1][0].getWeight()
            backPerceptron.setBackPropagate(False, last, weight[backPerceptronIndex + 1])
          backPerceptron.updateWeight()

  def getLevelPerceptronOutput(self, perceptronItems):
    eLevelOutputData = [-1]
    for item in perceptronItems:
      eLevelOutputData.append(item.getEOutput())
    return eLevelOutputData

  def checkWeight(self, eValue, eOutput):
    regexE = self.getRegexEValue()
    minRange = regexE[eValue]['minRange']
    maxRange = regexE[eValue]['maxRange']
    if minRange < eOutput < maxRange:
        return True
    else:
        return False

  def setRegexEValue(self, eVal):
    allEValue = eVal
    # allEValue = [0, 1]
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
    self.__REGEX_E_VALUE = temp


  def getRegexEValue(self):
    return self.__REGEX_E_VALUE

  def calcu(self, inputData, weight):
    # temp1 = inputData[1] * weight[1]
    # temp2 = inputData[2] * weight[2]
    # expNum = temp1 + temp2 - weight[0]
    expNum = np.dot(inputData, weight)
    sigmoidalNum = 1 / (1 + math.exp(-1 * expNum))
    return sigmoidalNum

  def printWeight(self):
    for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL):
      print('------')
      for itemIndex, item in enumerate(level):
        print('level:', levelIndex, 'weight:', itemIndex, 'output', item.getEOutput())
        print(item.getWeight())
        print(item.getWeight())
    print(self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput())