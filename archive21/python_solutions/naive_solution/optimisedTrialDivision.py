from time import time_ns
from math import sqrt, ceil

def optimisedTrialDivision(n: int = 273455) -> list[int]:
	primeFactorisation = {}

	if n % 2 == 0:
		primeFactorisation[2] = 0
		while int(n/2) == n/2:
			n /= 2
			primeFactorisation[2] += 1
		
	possiblePrimeFactor = 3
	while possiblePrimeFactor <= ceil(sqrt(n)):
		if n % possiblePrimeFactor == 0:
			primeFactor = possiblePrimeFactor
			primeFactorisation[primeFactor] = 0
			while int(n/primeFactor) == n/primeFactor:
				n /= primeFactor
				primeFactorisation[primeFactor] += 1
		possiblePrimeFactor += 2
	if n in primeFactorisation.keys():
		primeFactorisation[int(n)] += 1
	elif n > 1:
		primeFactorisation[int(n)] = 1
	return primeFactorisation

if __name__ == "__main__":
	startTime = time_ns()
	biggestDivisor = optimisedTrialDivision()
	stopTime = time_ns()
	print("answer: ", biggestDivisor, "\nTime Taken (ms): ", (stopTime - startTime) / 1000000)		
