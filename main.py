# Hw1
# from src.gui import UiLayout

# if __name__ == "__main__":
#     UiLayout.UiLayout()

# Hw2
from src.nerual.MultiPerceptron import MultiPerceptron
from src.gui.UiLayoutV2 import UiLayoutV2

if __name__ == "__main__":
    # ui = UiLayoutV2()

    pe = MultiPerceptron()
    pe.startTraining()