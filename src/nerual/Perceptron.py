import random
import numpy as np

from src.file.File import File
class Perceptron():

    def __init__(self, learnRate, endRound, fileName):
        print('Perceptron')
        self.__LEARN_RATE = learnRate
        self.__END_ROUND = endRound
        self.__DATA_WITH_WEIGHT = File().getFileContent(fileName)
        
        self.__DATA_LENGTH = len(self.__DATA_WITH_WEIGHT[0]) - 2
        self.__W = self.randomWeight()
        
        self.__E = []
        for i in self.__DATA_WITH_WEIGHT:
            if i[self.__DATA_LENGTH + 1] not in self.__E:
                self.__E.append(i[self.__DATA_LENGTH + 1])

        self.perceptronCalcu(self.__DATA_WITH_WEIGHT)

    def randomWeight(self):
        weight = []
        for count in range(0, self.__DATA_LENGTH + 1):
            weight.append( round( random.uniform(-1, 1), 2 ) )
        return weight

    def perceptronCalcu(self, originData):
        roundTime = 0
        while(roundTime < self.__END_ROUND):
            roundTime += 1
            # print("Round " + str(roundTime) + '----------------')

            index = 0
            end = True
            for dataWithWeight in originData:
                
                # print('------------' + 'round init ' + str(index))
                dataSetArr = dataWithWeight[:self.__DATA_LENGTH]
                # print('--i--')
                # print(i)
                # print('--calcu--')
                # print(self.__W)
                # print(dataSetArr)

                answer = np.dot(self.__W, dataSetArr)
                if self.checkValueIsRight(dataWithWeight, answer):
                    end = False
                    # print("------------------Change __W ---------------")
                    # print(self.__W)
                    # print(i)
                
                index += 1

            # print('--end--')
            # print(end)
            if end:
                roundTime = 1000
        print('perceptronCalcu')

    def checkValueIsRight(self, originData, answer):
        dataSetArea = self.__E
        answerIndex = self.__DATA_LENGTH + 1
        if answer < 0:
            if originData[answerIndex] != dataSetArea[0]:
                self.weightCrossLearnRate(originData[:self.__DATA_LENGTH], 1)
                return True
        elif answer >= 0:
            if originData[answerIndex] != dataSetArea[1]:
                self.weightCrossLearnRate(originData[:self.__DATA_LENGTH], 0)
                return True
        
        return False

    def weightCrossLearnRate(self, originData, calcuType):
        count = 0
        temp = []

        for i in originData:
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
        
        
                