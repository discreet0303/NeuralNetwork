
# from src.gui import UiLayout

# if __name__ == "__main__":
#     UiLayout.UiLayout()

from src.nerual.PerceptronV2 import PerceptronV2
import numpy as np

xorData = [
    [[-1, 0, 0], 0],
    [[-1, 0, 1], 1],
    [[-1, 1, 0], 1],
    [[-1, 1, 1], 0],
]

def mulitPerceptron():
    multiPerceptronModel = [
        [PerceptronV2(), PerceptronV2()],
        [PerceptronV2()]
    ]

    multiPerceptronModel[0][0].setWeight([-1.2, 1, 1])
    multiPerceptronModel[0][1].setWeight([0.3, 1, 1])
    multiPerceptronModel[1][0].setWeight([0.5, 0.4, 0.8])

    inputTemp = xorData[3]

    for levelCount, level in enumerate(multiPerceptronModel):
        for perceptron in level:
            if levelCount == 0:
                perceptron.setInputData(inputTemp)
            else:
                EOutput = getLevelPerceptronOutput(multiPerceptronModel[levelCount - 1])
                perceptron.setInputData([EOutput, 0])
    
    last = 0
    for levelIndex, level in enumerate(multiPerceptronModel[::-1]):
        # print(levelIndex)
        # print(backPerceptron)
        # print('-----------')
        
        for backPerceptronIndex, backPerceptron in enumerate(level):
            if levelIndex == 0:
                backPerceptron.setBackPropagate(True, 0, 0)
                last = backPerceptron.getBackPropagate()
            else:
                if backPerceptronIndex == 0:
                    backPerceptron.setBackPropagate(False, last, 0.4)
                elif backPerceptronIndex == 1:
                    backPerceptron.setBackPropagate(False, last, 0.8)

                # print(backPerceptron.getBackPropagate())

            backPerceptron.resetWeight()




    # print('10----------Start')
    # # print(multiPerceptronModel[1][0].getEOutput())
    # # print(test[1][0].getWeight())
    # test[1][0].setBackPropagate(True, 0, 0)
    # last = test[1][0].getBackPropagate()
    # test[1][0].resetWeight()
    # print('10----------')

    # print('00----------Start')
    # # print(test[0][0].getEOutput())
    # # print(test[0][0].getWeight())
    # test[0][0].setBackPropagate(False, last, 0.4)
    # test[0][0].resetWeight()
    # print('00----------End')

    # print('01----------Start')
    # # print(test[0][1].getEOutput())
    # # print(test[0][1].getWeight())
    # test[0][1].setBackPropagate(False, last, 0.8)
    # test[0][1].resetWeight()
    # print('01----------End')

    regexEValue()

def getLevelPerceptronOutput(perceptronItems):
    EOutputData = [-1]
    for item in perceptronItems:
        EOutputData.append(item.getEOutput())
    return EOutputData


def regexEValue():
    allEValue = [1, 2, -1]

    temp = {}
    num = 1 / len(allEValue)
    for index, value in enumerate(allEValue):
        temp.update({
            index: {
                'e': value,
                'minRange': index * num,
                'maxRange': (index + 1) * num
            }
        })


if __name__ == "__main__":
    mulitPerceptron()