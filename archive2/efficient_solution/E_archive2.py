from time import time_ns

def computeNextEvenTerm(previousEvenTerm: int, currentEvenTerm: int) -> int:
    nextTerm = previousEvenTerm + (4 * currentEvenTerm)
    return nextTerm

def sumEvenTerms(upperBound: int = 4000000) -> int:
    currentEvenTerm = 8
    previousEvenTerm = 2
    sum = 2
    while currentEvenTerm < upperBound:
        sum += currentEvenTerm
        nextEvenTerm = computeNextEvenTerm(previousEvenTerm, currentEvenTerm)
        previousEvenTerm, currentEvenTerm = currentEvenTerm, nextEvenTerm
    return sum

if __name__ == "__main__":
    startTime = time_ns()
    evenSum = sumEvenTerms()
    stopTime = time_ns()
    print(evenSum)
    print("Time taken for algorithm to execute in nanoseconds: " + str(stopTime - startTime))
