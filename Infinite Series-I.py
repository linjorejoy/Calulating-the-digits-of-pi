import math

def getPi(noOfTimes):
    piValue = 0
    for i in range(noOfTimes):
        numerator_1 = math.pow(math.factorial(2*i), 3)
        numerator_2 = 42*i + 5
        denominator_1 = math.pow(math.factorial(i), 6)
        denominator_2 = math.pow(16, 3*i + 1)
        piValue += numerator_1*numerator_2/(denominator_1*denominator_2)
    
    return 1/piValue

valueOfPi = getPi(1)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(2)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(3)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(5)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

valueOfPi = getPi(10)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))

