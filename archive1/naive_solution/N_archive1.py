import time


def sumOfAllMultiplesUnderN(multiple: int, N: int = 1000) -> int:
    sumOfMultiples = 0
    for integer in range(1, N):
        if (integer % multiple == 0):
            sumOfMultiples += integer
    return sumOfMultiples


if __name__ == "__main__":
    startTime = time.time_ns()
    sumOf3 = sumOfAllMultiplesUnderN(3)
    sumOf5 = sumOfAllMultiplesUnderN(5)
    sumOf15 = sumOfAllMultiplesUnderN(15)
    finalSum = (sumOf3 + sumOf5) - sumOf15 # application of PIE
    stopTime = time.time_ns()
    print(finalSum)
    print("Time taken in nanoseconds: " + str(stopTime - startTime))
