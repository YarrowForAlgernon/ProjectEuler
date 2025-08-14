from time import time_ns
from math import floor


class archive19:
    
    
    def __init__(this):

        this.yearLookup = {}
        this.dayOfWeek = 0
        this.sundayCount = 0
        this.yearCount = 1900


    def getDayOfWeek(this, month = 13, day = 1):

        monthCode = floor((13 * (month + 1)) / 5)
        dayOfWeek = day + monthCode + (this.yearCount-1) + floor((this.yearCount-1) / 4) - floor((this.yearCount-1) / 100) + floor((this.yearCount-1) / 400)
        dayOfWeek %= 7
        return dayOfWeek


   def checkEntryExists(this):
        '''two conditions - if leap year if current day of week dont exist.'''  
        sundayCounter = 0

        if this.dayOfWeek not in this.yearLookup:
            for month in range(3, 15):
                firstOfMonth = this.getDayOfWeek(month)
                if firstOfMonth == 1:
                    sundayCounter += 1
            this.yearLookup[this.dayOfWeek] = sundayCounter

    def checkLeapYear(this):
        if (this.yearCount % 4 == 0) and (this.yearCount % 100 != 0 or this.yearCount % 400 == 0):
            return True
        return False

    def incrementYear(this):
        this.yearCount += 1

    def leapYearAdjustment(this):
        if this.checkLeapYear():
            this.dayOfWeek += 7

    def incrementSundayCount(this):
        this.sundayCount += this.yearLookup[this.dayOfWeek]


    def calculateSolution(this):
        '''calculates all days that fall on the first of a month.'''

        while this.yearCount < 2001:

            this.dayOfWeek = this.getDayOfWeek()

            this.leapYearAdjustment()

            this.checkEntryExists()

            this.incrementSundayCount()

            this.incrementYear()

        return this.sundayCount


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateSolution()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))
