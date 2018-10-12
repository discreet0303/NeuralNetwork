import random
import numpy as np

from src.file.File import File
class Perceptron():

    def __init__(self, learnRate, endRound, fileName):
        self.__LEARN_RATE = learnRate
        self.__END_ROUND = endRound
        self.__DATA_WITH_WEIGHT, maxDataRange, minDataRange = File().getFileContent(fileName, -1)

        self.__DATA_FOR_TRAINING, self.__DATA_FOR_TESTING  = self.randomDataTo2Array(self.__DATA_WITH_WEIGHT)
        self.__DATA_LENGTH = len(self.__DATA_WITH_WEIGHT[0]) - 2
        self.__DATA_WITH_WEIGHT_LENGTH = self.__DATA_LENGTH + 1
        self.__W = self.randomWeight()
        
        self.__E = []
        for i in self.__DATA_WITH_WEIGHT:
            if i[self.__DATA_LENGTH + 1] not in self.__E:
                self.__E.append(i[self.__DATA_LENGTH + 1])

    def randomWeight(self):
        weight = []
        for count in range(0, self.__DATA_LENGTH + 1):
            weight.append( round( random.uniform(-1, 1), 2 ) )
        return weight

    def randomDataTo2Array(self, data):
        index = 0
        testingCount = int((len(data) / 3) * 1)
        dataForTraining = data[:]
        dataForTesting = []
        while testingCount != len(dataForTesting):
            trainingRange = len(dataForTraining) - 1
            index = random.randint(0, trainingRange)
            dataForTesting.append(dataForTraining[index])
            del dataForTraining[index]

        return dataForTraining, dataForTesting

    def perceptronCalcu(self, dataType):
        if dataType == 'all':
            dataType = self.__DATA_WITH_WEIGHT
        elif dataType == 'training':
            originData = self.__DATA_FOR_TRAINING
        elif dataType == 'testing':
            originData = self.__DATA_FOR_TESTING
        else:
            originData = []

        roundTime = 0
        while(roundTime < self.__END_ROUND):
            roundTime += 1

            index = 0
            end = True
            for dataWithWeight in originData:
                
                dataSetArr = dataWithWeight[:self.__DATA_WITH_WEIGHT_LENGTH]

                answer = np.dot(self.__W, dataSetArr)
                if self.checkValueIsRight(dataWithWeight, answer):
                    end = False
                
                index += 1

            if end:
                roundTime = 1000


    def checkValueIsRight(self, originData, answer):
        dataSetArea = self.__E
        answerIndex = self.__DATA_WITH_WEIGHT_LENGTH
        if answer < 0:
            if originData[answerIndex] != dataSetArea[0]:
                self.weightCrossLearnRate(originData[:self.__DATA_WITH_WEIGHT_LENGTH], 1)
                return True
        elif answer >= 0:
            if originData[answerIndex] != dataSetArea[1]:
                self.weightCrossLearnRate(originData[:self.__DATA_WITH_WEIGHT_LENGTH], 0)
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

    def getWeightYToZero(self):
        temp = []

        if self.__W[self.__DATA_LENGTH] == 0:
            self.__W = self.randomWeight()
            self.perceptronCalcu('training')

        for w in self.__W:
            temp.append( round(w / self.__W[self.__DATA_LENGTH], 2) )

        return temp
    
    def getWeight(self):
        return self.__W

    def getTestingDataIndex(self):
        temp = []
        for testingData in self.__DATA_FOR_TESTING:
            count = 0
            for data in self.__DATA_WITH_WEIGHT:    

                if testingData == data:
                    temp.append(count)
                count += 1

        return temp
    
    def getDataSuccessRate(self, rateType):
        if rateType == 'training':
            data = self.__DATA_FOR_TRAINING
        elif rateType == 'testing':
            data = self.__DATA_FOR_TESTING
        else:
            return 0

        dataSetArea = self.__E
        answerIndex = self.__DATA_WITH_WEIGHT_LENGTH
        count = 0

        for dataWithWeight in data:
            answer = np.dot(self.__W, dataWithWeight[:self.__DATA_WITH_WEIGHT_LENGTH])

            if answer < 0:
                if dataWithWeight[answerIndex] == dataSetArea[0]:
                    count += 1
            elif answer >= 0:
                if dataWithWeight[answerIndex] == dataSetArea[1]:
                    count += 1

        if count == 0:
            return 0
        else:
            return round( count / len(data) * 100, 2)