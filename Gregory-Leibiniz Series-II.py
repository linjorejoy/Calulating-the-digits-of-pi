
import math

def getPi(noOfIter):
    piValue = 1
    for i in range(1,noOfIter+1):
        piValue += (-1)**i * math.pow(math.pow((i+1),2),-1)
    return math.pow(piValue*12,1/2)


valueOfPi = getPi(100)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(1000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
