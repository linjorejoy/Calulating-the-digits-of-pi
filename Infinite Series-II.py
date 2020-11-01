import math

def getPi(noOfTimes):
    piValue = 0
    for i in range(noOfTimes):
        numerator_1 = ((-1)^i)*math.factorial(4*i)
        numerator_2 = 21460*i + 1123
        denominator_1 = math.pow(math.factorial(i), 4)
        denominator_2 = math.pow(441, 2*i + 1)
        denominator_3 = math.pow(2, 10*i + 1)
        piValue += numerator_1*numerator_2/(denominator_1*denominator_2*denominator_3)
    
    return 4/piValue

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

