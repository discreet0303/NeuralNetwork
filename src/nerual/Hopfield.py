import numpy as np
import math

class Hopfield():

    def __init__(self, data):
        self.data = data
        self.dataLen = len(data[0])

        self.setWeight()
        # print('-------------------')
        # print(self.weight)
        # print(self.rowSum)
        # print('-------------------')
        # self.calcu()

    def calcu(self, inputData):
        output = self.setOutput(inputData)
        sameTimesCount = 0
        for times in range(100):
            if not np.array_equal(inputData, output):
                inputData = output
                sameTimesCount = 0
            elif sameTimesCount == 2:
                continue
            else:
                sameTimesCount += 1
            output = self.setOutput(inputData)
            
        return output

    def setOutput(self, inputData):
        self.setWeight()
        output = np.dot(self.weight, inputData)
        for index, data in enumerate(output):
            num = np.around(data - self.rowSum[index], decimals = 5)
            if num > self.rowSum[index]:
                output[index] = 1
            elif num < self.rowSum[index]:
                output[index] = -1
            else:
                output[index] = inputData[index]
        
        return output


    def setWeight(self):
        weight = np.zeros((self.dataLen, self.dataLen), dtype = int)

        I = np.eye(self.dataLen)
        
        for data in self.data:
            weight += self.matrixCross(data)

        weight = weight * (1 / self.dataLen) - I * (len(self.data) / self.dataLen)
        self.weight = weight
        # self.rowSum = np.around(self.weight.sum(axis = 0), decimals = 5)
        self.rowSum = self.weight.sum(axis = 0)

    def matrixCross(self, data):
        mat = np.zeros((self.dataLen, self.dataLen), dtype = int)

        for x in range(self.dataLen):
            for y in range(self.dataLen):
                mat[x][y] = data[x] * data[y]
        
        return mat