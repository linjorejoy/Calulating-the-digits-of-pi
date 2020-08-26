"""This is from the BBP Formula which was discovered using the PSLQ Algorithm
"""

import math

def getPi(stepCount):
    stepSize = 1/stepCount
    piValue = 0
    yValue = 0
    while yValue<=1:
        piValue += ((16*yValue-16)*stepSize)/((yValue**4)-2*(yValue**3)+4*yValue-4)
        yValue += stepSize
    return piValue


valueOfPi = getPi(10000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
