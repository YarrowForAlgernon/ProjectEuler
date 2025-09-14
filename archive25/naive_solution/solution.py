from time import time_ns


class Solution:

	def __init__(this):

		this.NthTerm: int = 0
		this.binaryForm: list[bool] = []
		this.NthFibTerm: int = 0
	
		this.convertIntegerToBase2()
	

	def convertIntegerToBase2(this):
		'''Calculates the binary form of an unsigned integer 
		as a list of boolean values.'''

		Integer = this.NthTerm
		this.binaryForm = []
		while Integer > 0:
			if Integer % 2 != 0:                                                       
		    		this.binaryForm.append(True)
			else:
				this.binaryForm.append(False)
			Integer //= 2


	def fastDoubling(this) -> int:
		'''Returns the nth term in the fibonacci sequence starting from 0. 
		O(log2(n)).'''
		a = 0 #F0
		b = 1 #F1
		while this.binaryForm:
			mostSignificantBit = this.binaryForm[-1]
			c = a * ((2 * b) - a) #Identity F2n
			d = (a**2) + (b**2) #Identity F2n+1
			if not mostSignificantBit: # if bit is 0
				a, b = c, d
			else:
				a, b = d, c + d
			this.binaryForm.pop(-1)
		return a


	def main(this):
		
		while len(str(this.NthFibTerm)) < 1000:
			this.NthTerm += 1
			this.convertIntegerToBase2()
			this.NthFibTerm = this.fastDoubling()
		return this.NthTerm

if __name__ == "__main__":

	startTime = time_ns()
	answer = Solution()
	x = answer.main()
	stopTime = time_ns()
	print("Answer: ", x, "\nTime taken (ms): ", (stopTime - startTime) / 1000000)
