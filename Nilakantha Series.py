"""This is from the Nilakantha Series [Referance:https://www.mathscareers.org.uk/article/calculating-pi/]

    pi = 3 +    4        4         4           4   
              ____  -  ____   +   ____    -   ____   +   .....
              2*3*4    4*5*6     6*7*8        8*9*10
"""

import math

def getPi(noOfIter):
    pivalue = 3
    for i in range(1, noOfIter+3):
        pivalue += 4/(2*i*(2*i+1)*(2*i+2))*((-1)**(i+1))
    
    return pivalue


piVal = getPi(10)
print("{0:.50f} and diff is {1}".format(piVal, piVal- math.pi))