#naive solution, without abstraction and magic numbers

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
    sum3 = sumOf3()
    sum5 = sumOf5()
    print(sum3)
    print(sum5)
    finalSum = sum3 + sum5
    print(finalSum)
