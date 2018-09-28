import os

class File():

    def __init__(self):
        print('file init') 
        self.__BASE_DIR_PATH = os.getcwd()
        self.__DATASET_DIR_PATH = os.path.join(self.__BASE_DIR_PATH, 'dataSet')

    def getFileContent(self):

        filePath = os.path.join(self.__DATASET_DIR_PATH, 'perceptron1.txt')
        
        with open(filePath, 'r') as dataSet:
            originData = dataSet.read().split('\n')

        dataDict = {}
        count = 1
        for data in originData:
            dataLen = len(data.split())
            arr = []
            for i in data.split():
                arr.append(i)
            
            dataDict[count] = arr
            count = count + 1

        print(dataDict)
        print(originData)

        print('get file cotent')