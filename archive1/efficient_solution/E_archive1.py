#the goal is to reduce it to a summation equation.
#the equation of a summation is 1/2 * n * (n+1)
#in order to reach this, we factor out what we are trying to divide by.

def SumOfDivisibility(divisor: int, dividend: int=999) -> float:
    quotient = dividend // divisor
    sum = divisor * (0.5 * quotient * (quotient+1))
    return sum

if __name__ == "__main__":
    finalSum = SumOfDivisibility(3) + SumOfDivisibility(5) - SumOfDivisibility(15)
    print(finalSum)
