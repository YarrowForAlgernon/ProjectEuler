def computeNextEvenTerm(previous3rdTerm: int, currentTerm: int) -> int:
    nextTerm = previous3rdTerm + (4 * currentTerm)
    return nextTerm

def sumEvenTerms():
    currentTerm = 8
    previousTerm = 2
    sum = 2
    while currentTerm < 4000000:
        sum += currentTerm 
        nextTerm = computeNextEvenTerm(previousTerm, currentTerm)
        previousTerm = currentTerm
        currentTerm = nextTerm
    return sum

if __name__ == "__main__":
    evenSum = sumEvenTerms()
    print(evenSum)
