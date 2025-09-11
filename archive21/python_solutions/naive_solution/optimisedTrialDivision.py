from time import time_ns
from math import sqrt, ceil

def optimisedTrialDivision(n: int = 600851475143):
	primeFactors = []

	if n % 2 == 0:
		primeFactors.append(2)
		n /= 2
		
	possiblePrimeFactor = 3
	while possiblePrimeFactor <= ceil(sqrt(n)):
		if n % possiblePrimeFactor == 0:
			primeFactors.append(possiblePrimeFactor)
			n /= possiblePrimeFactor
		possiblePrimeFactor += 2
	if n > 1:
		primeFactors.append(n)
	return max(primeFactors)

if __name__ == "__main__":
	startTime = time_ns()
	biggestDivisor = optimisedTrialDivision()
	stopTime = time_ns()
	print("answer: ", biggestDivisor, "\nTime Taken (ms): ", (stopTime - startTime) / 1000000)		
