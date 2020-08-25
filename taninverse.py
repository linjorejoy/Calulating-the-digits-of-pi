""" This is from the inverse trignometric function tan inverse 
    and its expansion
"""

import math

def getPi(stepCount):
    stepSize = 1/stepCount
    piValue = 0

    xValue = 0
    while xValue<=1:
        piValue += stepSize/(1+xValue**2)
        xValue += stepSize
    piValue *= 4
    return piValue

valueOfPi = getPi(100)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(1000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(10000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(100000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(1000000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(10000000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
