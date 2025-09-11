# Create a sieve, then divide by each prime.
# To extract each prime from the list, do we need to iterate over it?
from time import time_ns
from math import sqrt, ceil

def sieveOfEratosthenes(n: int) -> list[int]:
	sqrtOfN = ceil(sqrt(n))
	potentialPrimeList = [False,]*2
	potentialPrimeList.extend([True,]*(sqrtOfN))
	allPrimes = []

	for potentialPrime in range(2, sqrtOfN):
		if not potentialPrimeList[potentialPrime]:
			continue

		allPrimes.append(potentialPrime)

		for nonPrime in range(potentialPrime**2, sqrtOfN, potentialPrime):
			potentialPrimeList[nonPrime] = False
	return allPrimes


def getPrimeFactorisation(n: int) -> int:
	listOfPrimes = sieveOfEratosthenes(n)
	listOfPrimeFactors = []
	for primeNumber in listOfPrimes:
		if n % primeNumber == 0:
			listOfPrimeFactors.append(primeNumber)
			n /= primeNumber
	return max(listOfPrimeFactors)

	
if __name__ == "__main__":
	startTime = time_ns()
	x = getPrimeFactorisation(600851475143)
	stopTime = time_ns()
	print("Answer: ", x, "\nTime Taken (ms): ", (stopTime - startTime) / 1000000)
