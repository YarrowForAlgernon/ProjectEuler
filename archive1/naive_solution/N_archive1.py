import time

def sumOf3():
    sum = 0
    for number in range(1, 1000):
        if (number % 3 == 0):
                sum += number
    return sum

def sumOf5():
    sum = 0
    for number in range(1, 1000):
        if (number % 5 == 0) and (number % 3 != 0):
                sum += number
    return sum

if __name__ == "__main__":
    startTime = time.time_ns()
    sum3 = sumOf3()
    sum5 = sumOf5()
    finalSum = sum3 + sum5
    print(finalSum)
    stopTime = time.time_ns()
    print("Time taken in nanoseconds: " + str(stopTime - startTime))
