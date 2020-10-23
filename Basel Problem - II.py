
import math

def nthTerm(n):
    return 1 / math.pow(n , 4)

def getPi(iterations):
    value = 0
    for i in range(1, iterations):
        value += nthTerm(i)
    
    piValue = math.pow(value*90 , 1/4)

    return piValue


valueOfPi = getPi(2)
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

valueOfPi = getPi(5000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
