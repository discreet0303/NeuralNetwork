import random
import numpy as np

class Perceptron():

    def __init__(self):
        print('Perceptron')
        self.__LEARN_RATE = 0.8
        self.__DATA = [
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, -1],
            [1, 1, 1]
        ]
        self.__DATA_LENGTH = len(self.__DATA[0]) - 1
        self.__W = self.randomWeight(self.__DATA_LENGTH)

        self.__E = [1, 0]

        self.perceptronCalcu(self.__DATA)

    def randomWeight(self, len):
        weight = []
        for count in range(0, len + 1):
            weight.append( round( random.uniform(-1, 1), 2 ) )
        # return weight
        return [-1, 0, 1]

    def perceptronCalcu(self, inputData):
        roundTime = 0
        while(roundTime < 5):
            roundTime += 1
            print("Round " + str(roundTime) + '----------------')

            index = 0
            for i in inputData:
                
                print('------------' + 'round init ' + str(index))
                print(i)
                print(self.__W)
                
                dataSetArr = [-1] + i[:2]
                answer = np.dot(self.__W, dataSetArr)
                self.checkValueIsRight(i, answer)
                
                index += 1

                print('------------' + 'answer round ' + str(index))
                print(answer)
                
                
                # self.checkValueIsRight(i, answer)

                # print(dataSetArr)
                # print(answer)
            
            print(self.__W)
        
        print('perceptronCalcu')

        # a = np.dot(inputData, self.__W)
        # self.weightCrossLearnRate(inputData)
        # self.checkValueIsRight(a, inputData)

    def checkValueIsRight(self, inputData, answer):
        dataSetArea = [1, -1]
        
        if answer >= 0:
            if inputData[2] != dataSetArea[0]:
                self.weightCrossLearnRate(inputData)
                return True
        elif answer < 0:
            if inputData[2] != dataSetArea[1]:
                self.weightCrossLearnRate(inputData)
                return True
        
        return False

    def weightCrossLearnRate(self, inputData):
        count = 0
        temp = []
        for i in inputData:
            # self.__W[count] = round( self.__W[count] - 0.8 * i, 2 )
            val = round( self.__W[count] - 0.8 * i, 2 )
            if val > 1:
                val = 1
            elif val <  -1:
                val = -1 
            temp.append(val)
            count += 1

        self.__W = temp
        
                