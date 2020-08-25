"""from half-area of the circle we get the below shown integral

"""

import math

def getPi(stepCount):
    pivalue = 0
    stepSize = 2/stepCount
    xValue = -1
    while xValue <= 1:
        pivalue += math.sqrt(1-math.pow(xValue,2))*stepSize
        xValue += stepSize
    
    return pivalue*2

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
