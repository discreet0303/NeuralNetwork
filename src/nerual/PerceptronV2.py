import random
import numpy as np
import math

class PerceptronV2:
    def __init__(self):
        print('PerceptronV2')
        
        self.__DATA = []
        self.__EOutput = -100
        self.__LEARN_RATE = 0.5
        self.__BACK_PROPAGATE = 0
        # self.randomWeight()

    def setInputData(self, inputData):
        self.__DATA = inputData
        self.__DATA_LENGTH = len(inputData[0]) - 1
        self.__DATA_LENGTH_WITH_PREFIX = len(inputData[0])
        self.setEOutput()

    def setEOutput(self):
        expNum = np.dot(self.__DATA[0], self.__W)
        sigmoidalNum = 1 / (1 + math.exp(-1 * expNum))
        self.__EOutput = sigmoidalNum
    
    def getEOutput(self):
        print(self.__EOutput)
        return self.__EOutput

    def randomWeight(self):
        # self.__W = []
        # for count in range(0, self.__DATA_LENGTH_WITH_PREFIX):
        #     self.__W.append( random.uniform(-1, 1) )
        self.__W = [-1.2, 1, 1]

    def getWeight(self):
        print(self.__W)
        return self.__W

    def setWeight(self, w):
        self.__W = w

    def setBackPropagate(self, outputLevel, preBackPropagate, weightValue):
        if outputLevel:
            self.__BACK_PROPAGATE = (self.__DATA[1] - self.__EOutput) * self.__EOutput * (1 - self.__EOutput)
            print('output level')
        else:
            self.__BACK_PROPAGATE = self.__EOutput * (1 - self.__EOutput) * preBackPropagate * weightValue
            print('preBackPropagate level')
        # print(self.__EOutput)
        # print(preBackPropagate)
        # print(weightValue)
        # print(self.__BACK_PROPAGATE)

    def getBackPropagate(self):
        return self.__BACK_PROPAGATE

    def resetWeight(self):
        temp = []

        for index, item in enumerate(self.__W):
            val = item + 0.5 * self.__BACK_PROPAGATE * self.__DATA[0][index]
            temp.append(val)
        
        self.__W = temp
        print(self.__W)

