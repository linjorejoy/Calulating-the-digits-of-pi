
import math

def getPi(noOfIter):
    piValue = 1
    for i in range(1,noOfIter+1):
        piValue += math.pow(math.pow((2*i+1),2),-1)
    return math.pow(piValue*8,1/2)


valueOfPi = getPi(10)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(100)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(500)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(1000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(2000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(5000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
