from src.nerual.MultiPerceptronItem import MultiPerceptronItem

import numpy as np
import math
class MultiPerceptron():

  def __init__(self):
    print('MultiPerceptron')
    self.__LEVEL = 3
    self.__ITEM = 2

    self.__END_ROUND = 1000
    self.__ERROR = 0

    self.__PERCEPTRON_MODEL = []
    for level in range(0, self.__LEVEL - 1):
      temp = []
      for item in range(0, self.__ITEM):
        temp.append(MultiPerceptronItem())
      self.__PERCEPTRON_MODEL.append(temp)
    self.__PERCEPTRON_MODEL.append([MultiPerceptronItem()])

  def startTraining(self, inputData, eValList):
    self.setRegexEValue(eValList)
    for count in range(self.__END_ROUND):
      self.__ERROR = 0
      for data in inputData:
        self.singleDataTraining(data)
      print("Count: ", count, '=> ', self.__ERROR)

    transPoint = []
    for pos in inputData:
      x = self.calcu(pos[0], self.__PERCEPTRON_MODEL[self.__LEVEL - 2][0].getWeight())
      y = self.calcu(pos[0], self.__PERCEPTRON_MODEL[self.__LEVEL - 2][1].getWeight())
      transPoint.append([[x, y], pos[1]])

    return transPoint, self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getWeight()

  def singleDataTraining(self, inputData):
    pos = inputData[0]
    eVal = inputData[1]
    for levelCount, level in enumerate(self.__PERCEPTRON_MODEL):
      for perceptron in level:
        if levelCount == 0:
          perceptron.setInputData(inputData)
        else:
          eOutput = self.getLevelPerceptronOutput(self.__PERCEPTRON_MODEL[levelCount - 1])
          perceptron.setInputData([eOutput, eVal])

    finalOutput = self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput()
    regexE = self.getRegexEValue()
    middleVal = regexE[eVal]['middleVal']
    # 均方誤差
    self.__ERROR = self.__ERROR + 0.5 * (finalOutput - middleVal) ** 2

    if not self.checkWeight(eVal, finalOutput):
      allModelWeight = self.getAllModelWeight()
      allBackPropagate = []
      for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL[::-1]):
        if levelIndex == 0:
          level[0].setBackPropagate(True, 0, middleVal, 0)
          allBackPropagate.append([level[0].getBackPropagate()])
        else:
          levelBackPropagate = []
          prevWeight = allModelWeight[self.__LEVEL - levelIndex]
          for backPerceptronIndex, backPerceptron in enumerate(level):
            backPerceptron.setBackPropagate(False, allBackPropagate[0], prevWeight, backPerceptronIndex)
            levelBackPropagate.append(backPerceptron.getBackPropagate())
          allBackPropagate = [levelBackPropagate] + allBackPropagate
      for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL):
        for perceptronIndex, perceptron in enumerate(level):
          perceptron.updateWeight()

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
    expNum = np.dot(inputData, weight)
    sigmoidalNum = 1 / (1 + math.exp(-1 * expNum))
    return sigmoidalNum

  def getAllModelWeight(self):
    data = []
    for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL):
      temp = []
      for itemIndex, item in enumerate(level):
        temp.append(item.getWeight())
      data.append(temp)
    return data

  def printWeight(self):
    for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL):
      print('------')
      for itemIndex, item in enumerate(level):
        print('level:', levelIndex, 'weight:', itemIndex, 'output', item.getEOutput())
        print(item.getWeight())
    print(self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput())

  def getDataCorrectRate(self, inputData):
    regexE = self.getRegexEValue()
    count = 0
    for data in inputData:
      point = data[0]
      eVal = data[1]
      middleVal = regexE[eVal]['middleVal']

      for levelCount, level in enumerate(self.__PERCEPTRON_MODEL):
        for perceptron in level:
          if levelCount == 0:
            perceptron.setInputData(data)
          else:
            eOutput = self.getLevelPerceptronOutput(self.__PERCEPTRON_MODEL[levelCount - 1])
            perceptron.setInputData([eOutput, eVal])

      finalOutput = self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput()

      if self.checkWeight(eVal, finalOutput):
        count += 1
    return count