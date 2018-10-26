
# from src.gui import UiLayout

# if __name__ == "__main__":
#     UiLayout.UiLayout()

from src.nerual.PerceptronV2 import PerceptronV2
import numpy as np
def mulitPerceptron():
    test = [
        [PerceptronV2(), PerceptronV2()],
        [PerceptronV2()]
    ]

    lastLevelIndex = len(test) - 1

    print(lastLevelIndex)

    test[0][0].setWeight([-1.2, 1, 1])
    test[0][1].setWeight([0.3, 1, 1])
    test[1][0].setWeight([0.5, 0.4, 0.8])

    for level in test:
        for perceptron in level:
            print(perceptron.getWeight())
    regexEValue()
    # a = PerceptronV2()
    # print(a.getWeight())
    # print(a.sigmoidal())

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

    print(temp)


if __name__ == "__main__":
    mulitPerceptron()