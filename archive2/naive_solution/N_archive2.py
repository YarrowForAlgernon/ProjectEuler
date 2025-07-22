import time

def getNextFibTerm(previousTerm: int, currentTerm: int) -> int:
    '''calculates the next term in the fibonacci sequence'''
    nextTerm = previousTerm + currentTerm
    return nextTerm

def checkIsEven(Term: int) -> bool:
    '''returns true if even, otherwise false'''
    return Term % 2 == 0

def sumTerms():
    '''gets the sum of all even fib terms under 4 million'''
    currentTerm = 1
    previousTerm = 0
    evenSum = 0
    while currentTerm < 4000000:
        nextTerm = getNextFibTerm(previousTerm, currentTerm)
        if checkIsEven(nextTerm):
            evenSum += nextTerm
        previousTerm = currentTerm
        currentTerm = nextTerm
    return evenSum


if __name__ == "__main__":
    startTime = time.time_ns()
    evenSum = sumTerms()
    stopTime = time.time_ns()
    print(evenSum)
    print("Time taken for algorithim to execute in nano seconds: " + str(stopTime - startTime))



