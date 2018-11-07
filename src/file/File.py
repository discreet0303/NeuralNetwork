import os

class File():

    def __init__(self):
        self.__BASE_DIR_PATH = os.getcwd()
        self.__DATASET_DIR_PATH = os.path.join(self.__BASE_DIR_PATH, 'dataSet')

    def getFileContentV2(self):
        filePath = os.path.join(self.__DATASET_DIR_PATH, '2Circle1.txt')

        with open(filePath, 'r') as dataSet:
            originData = dataSet.read().split('\n')

        dataArr = []
        eValList = []
        maxDataRange = minDataRange = 0
        for data in originData:
            if len(data.split()) == 0: continue
            arr = [-1]
            eVal = 0
            for dataIndex, i in enumerate(data.split()):
                if dataIndex == len(data.split()) - 1:
                    eVal = float(i)
                    if eVal not in eValList:
                        eValList.append(eVal)
                else:
                    arr.append(float(i))
            
            dataArr.append([arr, eVal])

        # print(dataArr)
        print('eValList')
        print(eValList)
        return dataArr, eValList


    def getFileContent(self, fileName, dataType):
        filePath = os.path.join(self.__DATASET_DIR_PATH, fileName)
        
        with open(filePath, 'r') as dataSet:
            originData = dataSet.read().split('\n')

        dataArr = []
        maxDataRange = minDataRange = 0
        for data in originData:
            if len(data.split()) == 0: continue

            if dataType == 1: arr = []
            elif dataType == -1: arr = [-1]

            for i in data.split():
                if float(i) > maxDataRange:
                    maxDataRange = float(i)
                if float(i) < minDataRange:
                    minDataRange = float(i)

                arr.append(float(i))
            
            dataArr.append(arr)

        return dataArr, maxDataRange, minDataRange

    def getFileContentWithIndex(self, fileName):
        filePath = os.path.join(self.__DATASET_DIR_PATH, fileName)
        
        with open(filePath, 'r') as dataSet:
            originData = dataSet.read().split('\n')

        dataArr = []
        dataLength = len(originData[0].split()) - 1
        for temp in range(0, dataLength):
            if len(temp) != 0:
                dataArr.append([])

        for data in originData:
            index = 0
            for i in data.split():
                if index < dataLength:
                    dataArr[index].append(i)
                index += 1
            
        print(dataArr)
        return dataArr

    def getDataSetFileName(self):
        disableName = ['IRIS.TXT', 'perceptron4.txt', 'perceptron3.txt', 'xor.txt', 'wine.txt', 'C3D.TXT', '4satellite-6.txt', 'Number.txt', '8OX.TXT', '5CloseS1.txt', 'C10D.TXT']

        dataFileArr = []
        for dataFile in os.listdir('./dataSet'):
            if dataFile not in disableName:
                dataFileArr.append(dataFile)
        
        return tuple(dataFileArr)