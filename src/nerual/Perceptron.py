import random
import numpy as np

class Perceptron():

    def __init__(self):
        print('Perceptron')
        self.__LEARN_RATE = 0.8
        self.__DATA = [
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 0],
            [1, 1, 0]
        ]
        self.dataLength = len(self.__DATA[0]) - 1
        self.__W = self.randomWeight(self.dataLength)

        self.perceptronCalcu(self.__DATA[3])

        # print(self.dataLength)
        # print(self.__W)
        # print(self.__DATA)

    def randomWeight(self, len):
        weight = []
        
        for count in range(0, len + 1):
            weight.append( round( random.uniform(-1, 1), 2 ) )

        return weight

    def perceptronCalcu(self, inputData):
        inputData = [-1] + inputData[:2]
        
        print(inputData)
        print(self.__W)
        a = np.dot(inputData, self.__W)
        print(a)

        print('perceptronCalcu')