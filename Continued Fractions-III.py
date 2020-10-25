

import math

def getPi(noOfIterations):
    piValue = math.pow(noOfIterations*2-1, 2) / (2)
    noOfIterations -= 1
    while(noOfIterations > 0):
        piValue = pow(noOfIterations*2-1, 2) / (2 + piValue)
        noOfIterations -= 1
    piValue += 1
    return 4/piValue


valueOfPi = getPi(3)
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
