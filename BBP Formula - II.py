"""This is from the BBP Formula which was discovered by F. Bellard
"""
import math

def getPi(noOfIter):
    piValue = 0 
    for n in range(noOfIter+1):
        firstTerm = 2**5/(4*n+1)
        secondTerm = 1/(4*n+3)
        thirdTerm = 2**8/(10*n+1)
        fourthTerm = 2**6/(10*n+3)
        fifthTerm = 2**2/(10*n+5)
        sixthTerm = 2**2/(10*n+7)
        seventhTerm = 1/(10*n+9)
        bracketContents = -firstTerm - secondTerm + thirdTerm - fourthTerm - fifthTerm - sixthTerm + seventhTerm
        piValue += (-1)**n/(2**(10*n))*bracketContents
    piValue /= 2**6
    return piValue

valueOfPi = getPi(100000)
print("{0:.50f} and difference is {1}".format(valueOfPi, valueOfPi-math.pi))
print("{0:.50f}".format(math.pi))
