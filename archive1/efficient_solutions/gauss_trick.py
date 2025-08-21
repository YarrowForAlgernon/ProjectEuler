import time

def SumOfMultiplesUnderN(multiple: int, N: int=999) -> float:
    quotient = N // multiple
    sumOfMultiples = multiple * (0.5 * quotient * (quotient+1))
    return sumOfMultiples

if __name__ == "__main__":
    startTime = time.time_ns()
    finalSum = SumOfMultiplesUnderN(3) + SumOfMultiplesUnderN(5) - SumOfMultiplesUnderN(15)
    stopTime = time.time_ns()
    print(finalSum)
    print("Time taken in nano seconds: " + str(stopTime - startTime))
