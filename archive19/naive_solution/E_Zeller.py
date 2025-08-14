from time import time_ns
from math import floor


class ZellersCongruence:

    def __init__(this, day, month, year):
        
        this.day = day
        this.month = month
        this.year = year
        this.adjustDates()

    def adjustDates(this):
        if this.month == 1 or this.month == 2:
            this.year -= 1
            this.month += 12

    def dayToTextConversion(this, dayOfWeek):
        dayOfWeekDict = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
        return dayOfWeekDict[dayOfWeek]

    
    def getDayOfWeek(this):

        monthCode = floor((13 * (this.month + 1)) / 5)
        print(monthCode)
        dayOfWeek = this.day + monthCode + this.year + floor(this.year / 4) - floor(this.year / 100) + floor(this.year / 400)
        dayOfWeek %= 7
        print(dayOfWeek)
        dayOfWeekString = this.dayToTextConversion(dayOfWeek)
        return dayOfWeekString


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

    
    def incrementWeek(this):
        this.dayCount += 7


    def incrementYear(this):
        this.yearCount += 1
        this.monthCount = 1


    def calculateDaysOnFirstOfMonth(this):
        '''calculates all days that fall on the first of a month.'''

        while this.yearCount  < 2100:

            this.incrementWeek()


            if this.checkDayCounterExceedsMonth():
                this.setDayCounter()

            if this.checkMonthCounterExceedsYear():
                this.incrementYear()
                this.checkLeapYear()

            this.checkForFirstSunday()

        return this.sundayCount - 2


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateDaysOnFirstOfMonth()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))
