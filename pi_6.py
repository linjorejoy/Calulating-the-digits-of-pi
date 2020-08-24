"""Gregory-Leibniz Series 
    pi / 4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ....
"""


def getPi(noOfIter):
    piValue = 1
    for i in range(1,noOfIter+1):
        # print((-1)**i * ((2*i+1)**(-1)))
        piValue += (-1)**i * ((2*i+1)**(-1))
    return piValue*4


print("{:.50f}".format(getPi(10000)))