from time import time_ns


class archive19:


    def __init__(this):

        this.monthToDayDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        this.dayCount = 7
        this.sundayCount = 0
        this.monthCount = 1
        this.yearCount = 1900


    def checkLeapYear(this):
        if (this.yearCount % 4 == 0) and (this.yearCount % 100 != 0 or this.yearCount % 400 == 0):
            this.monthToDayDict[2] = 29
        this.monthToDayDict[2] = 28


    def checkDayCounterExceedsMonth(this):
        return this.dayCount > this.monthToDayDict[this.monthCount]


    def setDayCounter(this):
        this.dayCount %= this.monthToDayDict[this.monthCount]
        this.monthCount += 1


    def checkMonthCounterExceedsYear(this):
        return this.monthCount > 12


    def checkForFirstSunday(this):
        if this.dayCount == 1:
            this.sundayCount += 1


    def incrementYear(this):
        this.yearCount += 1
        this.monthCount = 1


    def calculateDaysOnFirstOfMonth(this):
        '''calculates all days that fall on the first of a month.'''

        while this.yearCount  < 2001:

            this.dayCount += 7

            if this.checkDayCounterExceedsMonth():
                this.setDayCounter()

            if this.checkMonthCounterExceedsYear():
                this.incrementYear()
                this.checkLeapYear()

            this.checkForFirstSunday()

        return this.sundayCount


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateDaysOnFirstOfMonth()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))
