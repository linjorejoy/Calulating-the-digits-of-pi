"""From Basel Problem
    pi^2 / 6  =  sigma(n from 1 to inf) of 1/n^2
    
"""
import math

def getPi(noOfIter):
    piValue = 0
    for n in range(1,noOfIter+1):
        piValue += math.pow(n,-2)
    piValue *= 6
    piValue = math.sqrt(piValue)
    return piValue


pi_1 = getPi(1000)
print("pi = {0:.50f} and the error is {1:.50f}".format(pi_1, pi_1-math.pi))

pi_2 = getPi(10000)
print("pi = {0:.50f} and the error is {1:.50f}".format(pi_2, pi_2-math.pi))

pi_3 = getPi(100000)
print("pi = {0:.50f} and the error is {1:.50f}".format(pi_3, pi_3-math.pi))

pi_4 = getPi(1000000)
print("pi = {0:.50f} and the error is {1:.50f}".format(pi_4, pi_4-math.pi))

pi_1 = getPi(10000000)
print("pi = {0:.50f} and the error is {1:.50f}".format(pi_1, pi_1-math.pi))

pi_2 = getPi(100000000)
print("pi = {0:.50f} and the error is {1:.50f}".format(pi_2, pi_2-math.pi))