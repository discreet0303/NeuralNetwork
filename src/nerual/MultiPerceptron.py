from src.nerual.MultiPerceptronItem import MultiPerceptronItem

class MultiPerceptron():

  def __init__(self):
    print('MultiPerceptron')
    self.__LEVEL = 2
    self.__ITEM = 2

    self.__PERCEPTRON_MODEL = []
    for level in range(0, self.__LEVEL - 1):
      temp = []
      for item in range(0, self.__ITEM):
        temp.append(MultiPerceptronItem())
      self.__PERCEPTRON_MODEL.append(temp)
    self.__PERCEPTRON_MODEL.append([MultiPerceptronItem()])

    self.__PERCEPTRON_MODEL[0][0].setWeight([-1.2, 1, 1])
    self.__PERCEPTRON_MODEL[0][1].setWeight([0.3, 1, 1])
    self.__PERCEPTRON_MODEL[1][0].setWeight([0.5, 0.4, 0.8])

    # self.checkWeight(0, 0.4)

  def startTraining(self):
    xor = [
      [[-1, 1, 1], 0],
      [[-1, 0, 0], 0],
      [[-1, 0, 1], 1],
      [[-1, 1, 0], 1],
    ]

    self.singleDataTraining([[-1, 1, 1], 0])
    self.printWeight()
    # for count in range(0, 1000):
    #   for data in xor:
    #     self.singleDataTraining(data)
    #   print('Round', count)

  def singleDataTraining(self, inputData):
    for levelCount, level in enumerate(self.__PERCEPTRON_MODEL):
      for perceptron in level:
        if levelCount == 0:
          perceptron.setInputData(inputData)
        else:
          eOutput = self.getLevelPerceptronOutput(self.__PERCEPTRON_MODEL[levelCount - 1])
          perceptron.setInputData([eOutput, inputData[1]])
    
    finalOutput = self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0].getEOutput()

    if not self.checkWeight(inputData[1], finalOutput):
      last = 0
      for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL[::-1]):
        for backPerceptronIndex, backPerceptron in enumerate(level):
          if levelIndex == 0:
            backPerceptron.setBackPropagate(True, 0, 0)
            last = backPerceptron.getBackPropagate()
          else:
            if backPerceptronIndex == 0:
              backPerceptron.setBackPropagate(False, last, 0.4)
            elif backPerceptronIndex == 1:
              backPerceptron.setBackPropagate(False, last, 0.8)
          backPerceptron.updateWeight()
    
    finalOutput1 = self.__PERCEPTRON_MODEL[self.__LEVEL - 1][0]
    print(finalOutput1.getWeight())

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
                'minRange': index * num,
                'maxRange': (index + 1) * num
            }
        })
    return temp

  def printWeight(self):
    for levelIndex, level in enumerate(self.__PERCEPTRON_MODEL):
      print('------')
      for itemIndex, item in enumerate(level):
        print('level:', levelIndex, 'weight:', itemIndex)
        print(item.getWeight())