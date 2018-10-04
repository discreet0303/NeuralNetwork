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

        
        self.__E = []
        for i in self.__DATA:
            if i[self.__DATA_LENGTH] not in self.__E:
                self.__E.append(i[self.__DATA_LENGTH])

        self.perceptronCalcu(self.__DATA)

    def randomWeight(self, len):
        weight = []
        for count in range(0, len + 1):
            weight.append( round( random.uniform(-1, 1), 2 ) )
        return weight
        # return [-1, 0, 1]

    def perceptronCalcu(self, inputData):
        roundTime = 0
        while(roundTime < 20):
            roundTime += 1
            print("Round " + str(roundTime) + '----------------')

            index = 0
            end = True
            for i in inputData:
                
                print('------------' + 'round init ' + str(index))
                dataSetArr = [-1] + i[:2]
                print('--i--')
                print(i)
                print('--calcu--')
                print(self.__W)
                print(dataSetArr)

                answer = np.dot(self.__W, dataSetArr)
                if self.checkValueIsRight(i, answer):
                    end = False
                    print("------------------Change __W ---------------")
                    print(self.__W)
                    print(i)
                
                index += 1

                # print('------------' + 'answer round ' + str(index))
                # print(answer)
                
                
                # self.checkValueIsRight(i, answer)

                # print(dataSetArr)
                # print(answer)
            print('--end--')
            print(end)
            if end:
                roundTime = 1000
        print('perceptronCalcu')

    def checkValueIsRight(self, inputData, answer):
        dataSetArea = self.__E
        
        if answer < 0:
            if inputData[2] != dataSetArea[0]:
                inputData = [-1] + inputData[:2]
                self.weightCrossLearnRate(inputData, 1)
                return True
        elif answer >= 0:
            if inputData[2] != dataSetArea[1]:
                inputData = [-1] + inputData[:2]
                self.weightCrossLearnRate(inputData, 0)
                return True
        
        return False

    def weightCrossLearnRate(self, inputData, calcuType):
        count = 0
        temp = []

        for i in inputData:
            if calcuType == 0:
                val = round( self.__W[count] - 0.05 * i, 2 )
            else:
                val = round( self.__W[count] + 0.05 * i, 2 )

            if val > 1:
                val = 1
            elif val <  -1:
                val = -1 
            temp.append(val)
            count += 1

        self.__W = temp
        # print(temp)
        # print(self.__W)
        
        
                