from time import time_ns


def convertIntegerToBase2(Integer: int) -> list:
    '''Calculates the binary form of an unsigned integer 
    as a list of boolean values.
    '''
    binaryForm = []
    while Integer > 0:
        if Integer % 2 != 0:
            binaryForm.append(True)
        else:
            binaryForm.append(False)
        Integer //= 2
    return binaryForm


def fastDoubling(n: int) -> int:
    '''Returns the nth term in the fibonacci sequence starting from 0. 
    O(log2(n)).'''
    a = 0 #F0
    b = 1 #F1
    binaryForm = convertIntegerToBase2(n)
    while binaryForm:
        mostSignificantBit = binaryForm[-1]
        c = a * ((2 * b) - a) #Identity F2n
        d = (a**2) + (b**2) #Identity F2n+1
        if not mostSignificantBit: # if bit is 0
            a, b = c, d
        else:
            a, b = d, c + d
        binaryForm.pop(-1)
    return a


def main(n: int = 33) -> float:
    '''Returns the sum of all even Fibonacci terms under the nth term.'''
    n = setNthTermToEvenNumber(n)
    evenSummation = fastDoubling(n+2) - 1
    evenSummation //= 2 
    return evenSummation


def setNthTermToEvenNumber(n: int) -> int:
    '''Sets the value of n to a multiple of 3 to ensure it is
    an even number.'''
    return (n - (n % 3))

if __name__ == "__main__":
    startTime = time_ns()
    evenSum = main()
    stopTime = time_ns()
    print(evenSum, "\nNumber of digits: " + str(len(str(evenSum))), "\nTime (ms): " + str((stopTime - startTime) / 1000000))
