import random
import numpy as np
import math

class MultiPerceptronItem():
    
    def __init__(self):
        self.__DATA = []
        self.__W = []
        self.__LEARN_RATE = 0.01
        self.__BACK_PROPAGATE = 0

    def setInputData(self, inputData):
        self.__DATA = inputData
        self.__DATA_LENGTH = len(inputData[0]) - 1
        self.__DATA_LENGTH_WITH_PREFIX = len(inputData[0])
        if len(self.__W) != self.__DATA_LENGTH_WITH_PREFIX:
            self.randomWeight()
        self.setEOutput()

    def setEOutput(self):
        expNum = np.dot(self.__DATA[0], self.__W)
        sigmoidalNum = 1 / (1 + math.exp(-1 * expNum))
        self.__EOutput = sigmoidalNum
    
    def getEOutput(self):
        return round(self.__EOutput, 4)
        return self.__EOutput

    def randomWeight(self):
        self.__W = []
        for count in range(0, self.__DATA_LENGTH_WITH_PREFIX):
            self.__W.append( random.uniform(-1, 1) )

    def getWeight(self):
        return self.__W

    def setWeight(self, w):
        self.__W = w

    def setBackPropagate(self, outputLevel, preBackPropagate, weightValue, weightIndex):
        if outputLevel:
            self.__BACK_PROPAGATE = (weightValue - self.__EOutput) * self.__EOutput * (1 - self.__EOutput)
        else:
            sumTemp = 0
            for backPropagate in preBackPropagate:
                for weight in weightValue:
                    sumTemp += backPropagate * weight[weightIndex + 1]
            self.__BACK_PROPAGATE = self.__EOutput * (1 - self.__EOutput) * sumTemp
            
    def getBackPropagate(self):
        return self.__BACK_PROPAGATE

    def updateWeight(self):
        temp = []

        for index, item in enumerate(self.__W):
            val = item + self.__LEARN_RATE * self.__BACK_PROPAGATE * self.__DATA[0][index]
            temp.append(val)
        self.__W = temp

