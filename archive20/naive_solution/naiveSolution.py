from time import time_ns

class Solution:


	def __init__(this):

		this.NthFactorial = 47
		this.factorial = 1
		this.factorialDigitSum = 0
		this.calculateFactorial()
		this.calculateFactorialDigitSum()


	def calculateFactorial(this) -> None:
		for multiplication in range(1, this.NthFactorial+1):
			this.factorial *= multiplication


	def calculateFactorialDigitSum(this) -> None:
		for digit in str(this.factorial):
			this.factorialDigitSum += int(digit)


if __name__ == "__main__":
	startTime = time_ns()
	answer = Solution()
	stopTime = time_ns()
	print("Answer: ", answer.factorialDigitSum, f"\nThe Factorial of {answer.NthFactorial}: ", answer.factorial, "\nTime Taken (ms): ", (stopTime - startTime) / 1000000)
