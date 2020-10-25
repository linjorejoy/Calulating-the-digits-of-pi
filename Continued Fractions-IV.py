

import math
import timeit

def getPi(noOfIterations):
    piValue = math.pow(noOfIterations*4-2, 2) / (12)
    noOfIterations -= 1
    while(noOfIterations > 0):
        piValue = pow(noOfIterations*4-2, 2) / (12 + piValue)
        noOfIterations -= 1
    piValue += 6
    return piValue/2


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

valueOfPi = getPi(100000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
