"""This is by Archemedes method[Referance "https://youtu.be/DLZMZ-CT7YU"]
    pi = lim(n -> inf) n*sin(180/n)
"""

import math

def getPi(valueOfN):
    piValue = valueOfN*math.sin(math.radians(180/valueOfN))
    return piValue

piValue = getPi(10000000000)
print("{0:.50f} and diff is {1}".format(piValue, math.pi-piValue))


piValue2 = getPi(100000000000)
print("{0:.50f} and diff is {1}".format(piValue2, math.pi-piValue2))