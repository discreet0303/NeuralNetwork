import os

class File():

    def __init__(self):
        self.__BASE_DIR_PATH = os.getcwd()
        self.__DATASET_DIR_PATH = os.path.join(self.__BASE_DIR_PATH, 'dataSet')
    
    def getHopfieldData(self, fileName):
        filePath = os.path.join(self.__DATASET_DIR_PATH, fileName)

        with open(filePath, 'r') as dataSet:
            originData = dataSet.read().split('\n')

        dataArr = []
        arr = []
        lineCount = 0
        dataCount = 1
        if fileName == 'Bonus_Training.txt':
            rowNum = 10
        else: 
            rowNum = 12

        for data in originData:
            if len(data) > 0:
                for item in data:
                    if item == ' ':
                        arr.append(-1)
                    elif item == '1':
                        arr.append(1)
            elif len(data) == 0:
                dataArr.append(arr)
                arr = []
                dataCount += 1

        dataArr.append(arr)
                
        return dataArr, dataCount
        

    def getFileContentV2(self, fileName):
        filePath = os.path.join(self.__DATASET_DIR_PATH, fileName)

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
                    if eVal > maxDataRange:
                        maxDataRange = eVal
                    if eVal < minDataRange:
                        minDataRange = eVal

                    if eVal not in eValList:
                        eValList.append(eVal)
                else:
                    arr.append(float(i))
            
            dataArr.append([arr, eVal])
        
        # for data in dataArr:
        #     for itemIndex, item in enumerate(data[0]):
        #         if itemIndex == 0: continue
        #         else:
        #             item = (item - minDataRange) / (maxDataRange - minDataRange)

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
        disableName = []
        # disableName = ['IRIS.TXT', 'wine.txt', '4satellite-6.txt', 'Number.txt', '8OX.TXT', '5CloseS1.txt', 'C10D.TXT']

        dataFileArr = []
        for dataFile in os.listdir('./dataSet'):
            if dataFile not in disableName:
                dataFileArr.append(dataFile)
        
        return tuple(dataFileArr)