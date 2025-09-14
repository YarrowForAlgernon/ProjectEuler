# a couple of things:
#1.) an integer factorisation algorithm
# 1.1.) prime factorisation algorithm
# 1.2.) a way to combine all prime factors to get all possible factors
# 2.) naively iterate until we get n pairs of amicable numbers.



from optimisedTrialDivision import optimisedTrialDivision
from math import pow


def convertIntegerToBase2(Integer: int) -> list:
    '''Calculates the binary form of an unsigned integer 
    as a list of boolean values.
    '''                        
    binaryForm = []                                                                
    while Integer > 0:           
        if Integer % 2 != 0:                                                       
            binaryForm.append(1)
        else:           
            binaryForm.append(0)
        Integer //= 2
    return binaryForm

#get no of prime factors, raise 2 ** no. of prime factors, then keep incrementing it.

def updateDict(dictionary, binaryForm):	
	dictionary = {primeFactor: 0 for primeFactor in dictionary}
	print("current Form: ", binaryForm)
	for primeFactor, power in dictionary.items():
		dictionary[primeFactor] = binaryForm[-1]
		print(dictionary[primeFactor])
		binaryForm.pop(-1)
		if not binaryForm:
			return dictionary
	return dictionary

def getCompleteFactorisation(n):
	completeFactorisation: list[int] = [1]
	primeFactorisation: list[int] = optimisedTrialDivision(n)
	print(primeFactorisation)
	for primeFactor in primeFactorisation.keys():
		completeFactorisation.append(primeFactor)
	start = 1
	end = pow(2, len(primeFactorisation)-1) - 1
	binaryForm = convertIntegerToBase2(start)
	print(binaryForm)
	newDict = {}
	for primeFactor in primeFactorisation:
		newDict[primeFactor] = 0
	updateDict(newDict, binaryForm)
	print("newDict: ", newDict)
	while start <= end:
		newFactor = 1
		for primeFactor, power in newDict.items():
			print("prime Factor: ", primeFactor, " power: ", power, " result: ", pow(primeFactor, power))
			newFactor *= pow(primeFactor, power)
			print(newFactor)
		start += 1
		binaryForm = convertIntegerToBase2(start)
		updateDict(newDict, binaryForm)
		print(newDict)
		print(newFactor)
		print(binaryForm)
		completeFactorisation.append(int(newFactor))
	
	print("rn: ", completeFactorisation, primeFactorisation)
	completeCopy = completeFactorisation.copy()
	for primeFactor in primeFactorisation.keys():
		while primeFactorisation[primeFactor] > 0:
			for existingFactor in completeCopy:
				completeFactorisation.append(int(existingFactor * primeFactor))
			primeFactorisation[primeFactor] -= 1
	return set(completeFactorisation)


def findAmicablePairs():
	pass
	#numberOfPairs = 0
	#for integer in range(2, 10000):
	#	listOfAllFactors = getCompleteFactorisation(integer)
		
if __name__ == "__main__":
	x = getCompleteFactorisation(220)
	print(x)
