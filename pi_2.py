"""from Matt Parkers Youtube video "https://www.youtube.com/watch?v=LhlqCJjbEa0"
    called Chudnovsky algorithm 

                           426880 * sqrt(10005)
 pi =       ______________________________________________________
            sigma(k=0,inf) of   [(6k)! * (545140134k + 13591409)]
                              _______________________________________
                             (3k)! * (k!)^3 * (-262537412640768000)^k
""" 
import math
import decimal

def getPi(noOfIter):
    piValue = 426880* math.sqrt(10005)
    denominatorValue = 0
    for k in range(noOfIter):
        numerator = math.factorial(6*k) * (545140134*k + 13591409)
        denominator = math.factorial(3*k) * (math.factorial(k))**3 * ((-262537412640768000)**k)
        denominatorValue += numerator/denominator
        
    piValue /= denominatorValue
    return piValue


# print(math.factorial(0))

print("{0:.50f}".format(getPi(20)))
print("{0:.50f}".format(math.pi))

print("*"*50)

print("the difference is {}".format(getPi(20) - math.pi))