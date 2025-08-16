from time import time_ns

class archive19:


    def __init__(this):

        this.monthToDayDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        this.dayCounter = 6
        this.sundayCounter = 0
        this.monthCounter = 1
        this.currentYear = 1901
        this.endYear = 2001


    def checkLeapYear(this):
        '''If the year is a leap year, change the number of days in 
        February from 28 days to 29 days.'''
        if (this.currentYear % 4 == 0) and (this.currentYear % 100 != 0 or this.currentYear % 400 == 0):
            this.monthToDayDict[2] = 29
        else:
            this.monthToDayDict[2] = 28


    def checkDayCounterExceedsMonth(this):
        return this.dayCounter > this.monthToDayDict[this.monthCounter]


    def rollOverDayCounter(this):
        '''Take the current dayCounter modulo the number of days in 
        the month. The end result is the first sunday in the next month.'''
        this.dayCounter %= this.monthToDayDict[this.monthCounter]
        this.monthCounter += 1


    def checkMonthCounterExceedsYear(this):
        return this.monthCounter > 12


    def checkForFirstSunday(this):
        if this.dayCounter == 1:
            this.sundayCounter += 1

    
    def incrementWeek(this):
        this.dayCounter += 7


    def incrementYear(this):
        this.currentYear += 1
        this.monthCounter = 1


    def calculateSolution(this):
        '''calculates all sundays that fall on the first of a month
        in the years between 1901 and 2001.'''

        while this.currentYear  < this.endYear:

            this.incrementWeek()

            if this.checkDayCounterExceedsMonth():
                this.rollOverDayCounter()

            if this.checkMonthCounterExceedsYear():
                this.incrementYear()
                this.checkLeapYear()

            this.checkForFirstSunday()

        return this.sundayCounter


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateSolution()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))

