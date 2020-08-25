"""Spigot Algorithm to find the digits of pi
"""


import math

def getPi(noOfIter):
    piValue = 0
    for k in range(noOfIter+1):
        secondPart = 4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)
        piValue += (1/(math.pow(16,k)))*secondPart
    return piValue

valueOfPi = getPi(1)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(2)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(3)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(4)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(5)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(6)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(7)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(8)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(9)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(10)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(255)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

# limit : The below code will show OverFlowError
# valueOfPi = getPi(256)
# print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))