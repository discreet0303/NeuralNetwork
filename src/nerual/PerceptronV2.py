import random
import numpy as np
import math

class PerceptronV2:

    def __init__(self):
        print('PerceptronV2')
        
        self.__DATA = [ 
            [-1, 0, 0],
            [-1, 0, 1],
            [-1, 1, 0],
            [-1, 1, 1]
        ]

        self.__DATA_LENGTH = len(self.__DATA[0]) - 1
        self.__DATA_LENGTH_WITH_PREFIX = self.__DATA_LENGTH + 1

        # self.randomWeight()

    def randomWeight(self):
        # self.__W = []
        # for count in range(0, self.__DATA_LENGTH_WITH_PREFIX):
        #     self.__W.append( random.uniform(-1, 1) )
        self.__W = [-1.2, 1, 1]

    def getWeight(self):
        return self.__W

    def setWeight(self, w):
        self.__W = w

    def sigmoidal(self):
        expNum = np.dot(self.__DATA[3], self.__W)
        sigmoidalNum = 1 / (1 + math.exp(-1 * expNum))

        return sigmoidalNum