"""Srinivasa Ramanujan's method based on Modular Arithmetic ["https://en.wikipedia.org/wiki/Pi"]
"""


import math

def getPi(noOfIter):
    piValue = 0
    for k in range(noOfIter+1):
        numerator = math.factorial(4*k)* (1103+26390*k)
        denominator = math.pow(math.factorial(k),4)*math.pow(396,4*k)
        piValue += numerator/denominator
    piValue *= 2*math.sqrt(2)/9801
    piValue = math.pow(piValue,-1)
    return piValue


valueOfPi = getPi(1)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(2)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(3)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

