from math import log
from time import time_ns
import sys



def calculateBinaryForm(number: int) -> list:
    '''Calculates the binary form of an unsigned integer 
    as a list of boolean values.
    '''
    binaryArray = []
    while number > 0:
        if number % 2 != 0:
            binaryArray.append(True)
        else:
            binaryArray.append(False)
        number //= 2
    binaryArray.reverse()
    return binaryArray


def fastDoubling(n: int) -> int:
    '''returns the nth term in the fibonacci sequence starting from 0. 
    O(log2(n)).'''
    a = 0
    b = 1
    nBinaryForm = calculateBinaryForm(n)
    while nBinaryForm:
        n = nBinaryForm[0]
        c = a * ((2 * b) - a)
        d = (a**2) + (b**2)
        if not n: # if bit is 0
            a, b = c, d
        else:
            a, b = d, c + d
        nBinaryForm.pop(0)
    return a


def sumEvenTerms(n: int) -> float:
    '''Only works if the value of n is a multiple of 3 and therefore 
    a positive term. A quotient division is used to save time and
    space in divisions involving large numbers.'''
    isOdd = False
    evenSum = fastDoubling(n+2) - 1
    if evenSum % 2 != 0:
        isOdd = True
    evenSum //= 2 
    if isOdd:
        evenSum += 0.5
    return evenSum


def main(n: int = 33) -> int:
    '''if n isn't an even term, it will set it to the last even term, 
    in order to calculate the sum of all previous even terms.'''
    if n % 3 != 0:
        n = n - (n % 3)
    finalSum = sumEvenTerms(n)
    return finalSum


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    startTime = time_ns()
    evenSum = main()
    stopTime = time_ns()
    print(evenSum, "\nNumber of digits: " + str(len(str(evenSum))), "\nTime (ns): " + str(stopTime - startTime))
