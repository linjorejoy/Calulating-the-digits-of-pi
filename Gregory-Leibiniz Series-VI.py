
import math

def getPi(noOfIter):
    piValue = 1
    for i in range(1,noOfIter+1):
        piValue += (-1)**i *math.pow(math.pow((2*i+1),5),-1)
    return math.pow(piValue*1538/5, 1/5)


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
