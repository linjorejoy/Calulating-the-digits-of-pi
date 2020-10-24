

import math


def getPi(noOfIteratios):
    piValue = math.pow(noOfIteratios*2 - 1, 2) / 6
    noOfIteratios -= 1
    while(noOfIteratios > 0):
        piValue = math.pow(noOfIteratios*2 - 1, 2) / (piValue + 6)
        noOfIteratios -= 1
    return piValue + 3


valueOfPi = getPi(1)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(10)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(20)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(50)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(100)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(1000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
