import os

class File():

    def __init__(self):
        self.__BASE_DIR_PATH = os.getcwd()
        self.__DATASET_DIR_PATH = os.path.join(self.__BASE_DIR_PATH, 'dataSet')

    def getFileContent(self, fileName):
        filePath = os.path.join(self.__DATASET_DIR_PATH, fileName)
        
        with open(filePath, 'r') as dataSet:
            originData = dataSet.read().split('\n')

        dataArr = []
        count = 1
        for data in originData:
            dataLen = len(data.split())
            arr = [-1]
            for i in data.split():
                arr.append(i)
            
            dataArr.append(arr)

        print(dataArr)
    
    def sortFileContentWithIndex(self, fileName):
        filePath = os.path.join(self.__DATASET_DIR_PATH, fileName)
        
        with open(filePath, 'r') as dataSet:
            originData = dataSet.read().split('\n')

        dataArr = []
        dataLength = len(originData[0].split()) - 1
        for temp in range(0, dataLength):
            dataArr.append([])

        for data in originData:
            index = 0
            for i in data.split():
                if index < dataLength:
                    dataArr[index].append(i)
                index += 1
            
        print(dataArr)
    

    def getDataSetFile(self):
        dataFileArr = []
        for dataFile in os.listdir('./dataSet'):
            dataFileArr.append(dataFile)

        return tuple(dataFileArr)