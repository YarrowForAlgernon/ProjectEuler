# number letter counts.

from time import time_ns

class LetterCounts:
	
	def __init__(this):
	
		this.totalLettersUsed = 0
		this.currentNumber = 0
		this.endNumber = 1001
		this.thousandths = 0
		this.hundredths = 0
		this.tens = 0
		this.ones = 0
		this.numberToWord = ""
		this.numberToWordDictionary = {0: "", 1: "one", 2: "two", 3: "three", 
		4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
		10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
		15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
		19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
		60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"} 

		this.calculateNumberWord()


	def calculateThousandths(this):
		
		while this.currentNumber >= 1000:
			this.thousandths = this.currentNumber // 1000
			this.currentNumber -= 1000
		
		returnString = this.numberToWordDictionary[this.thousandths] + " thousand "
		return returnString

	def calculateHundreadths(this):
		if this.currentNumber >= 100 and this.currentNumber < 1000:
			this.hundreadths = this.currentNumber // 100
			this.currentNumber -= (this.hundreadths * 100)
		returnString = this.numberToWordDictionary[this.hundreadths] + " hundred"
		if this.currentNumber > 0:
			returnString += " and "
		return returnString

	def calculateTenths(this):
		if this.currentNumber < 100 and this.currentNumber >= 20:
			this.tens = this.currentNumber // 10
			this.tens *= 10
			this.currentNumber -= this.tens
		elif this.currentNumber >= 10 and this.currentNumber < 20:
			returnString = this.numberToWordDictionary[this.currentNumber]
			this.currentNumber = 0
			return returnString
		returnString = this.numberToWordDictionary[this.tens] + " "
		return returnString

	def calculateOnes(this):
		return this.numberToWordDictionary[this.currentNumber]

	def calculateNumberWord(this):

		for number in range(1,this.endNumber):
			this.currentNumber = number
			if this.currentNumber >= 1000:
				this.numberToWord += this.calculateThousandths()
			if this.currentNumber >= 100:
				this.numberToWord += this.calculateHundreadths()
			if this.currentNumber >= 10:
				this.numberToWord += this.calculateTenths()
			this.numberToWord += this.calculateOnes()
			this.numberToWord = this.numberToWord.replace(" ", "")
			this.totalLettersUsed += len(this.numberToWord)
			this.numberToWord = ""


if __name__ == "__main__":
	startTime = time_ns()
	answer = LetterCounts()
	stopTime = time_ns()
	print("answer: ", answer.totalLettersUsed, "\nTime taken (ms): ", (stopTime - startTime) / 1000000)
