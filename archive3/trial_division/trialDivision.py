from time import time_ns
from math import sqrt, ceil

def trialDivision(n: int = 600851475143):
	primeFactors = []
	loopCounter = 1
	while loopCounter <= n:
		if n % loopCounter == 0:
			primeFactors.append(loopCounter)
			n /= loopCounter
		loopCounter += 1
	return max(primeFactors)

if __name__ == "__main__":
	startTime = time_ns()
	biggestDivisor = trialDivision()
	stopTime = time_ns()
	print("answer: ", biggestDivisor, "\nTime Taken (ms): ", (stopTime - startTime) / 1000000)		
