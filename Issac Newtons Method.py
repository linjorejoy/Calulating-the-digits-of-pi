"""This is from the Youtube video  "https://www.youtube.com/watch?v=CKl1B8y4qXw" 
By Matt Parker in Stand-up Math Youtube channel to 
Find the digits of Py
"""
import math


def pi_iter(n):
    """Call this function to get the value of pi

    Args:
        n (integer): The number of iteration to which 
                     pi should be calculated.
    """
    pi_value = 3*math.sqrt(3)/4
    bin_exp = secondPartOfExp(0.25,0.5,n)
    for i in range(1,n):
        pi_value += 24*next(bin_exp)
        pass
    print("{0:.50f}".format(pi_value))
    return pi_value


def secondPartOfExp(x,n,noOfIter):
    """This is a modification to the binary expantion required in this case
        (1+x)^n = 

    Args:
        x (float): the value x in the expantion
        n (float): the value n in the expantion
        noOfIter (int): the number of iteration to be done

    Yields:
        float: each of the seperate elements of expantion
    """     
    for i in range(noOfIter):
        currTerm = 1
        for j in range(0,i):
            currTerm *= (j-n)/(j+1)
        fraction = (i + 1.5)
        currTerm *= x**(fraction)
        currTerm /= fraction
        yield currTerm
    pass

pi = pi_iter(1000)
print("{0:.50f}".format(math.pi))
print("The error is {}".format(math.pi-pi))