

import math

    
def doublefactorial(n):
     if n <= 0:
         return 1
     else:
         return n * doublefactorial(n-2)

def getPi(noOfIter):
    piValue = 1
    for i in range(1, noOfIter):
        piValue += math.factorial(i)/doublefactorial(2*i + 1)
    
    return piValue*2

valueOfPi = getPi(2)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(100)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(500)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(800)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
