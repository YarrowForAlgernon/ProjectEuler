from time import time_ns

class archive19:


    def __init__(this):
        '''Their are 14 unique years in the Gregorian calendar,
        meaning there are 14 configurations in which the days of
        the week occupy the same numerical days in a year. The way
        to distinguish between unique years is whether it is a leap 
        year and what day of the week it starts with.

        :param this.yearLookup:
            This is a dictionary whose key values represent the
            days of the week (0 = saturday). Their corresponding
            values are the number of sundays that fall on the first
            of each month in that year.
        :param this.leapYearLookup:
            This is a dictionary whose key values represent the
            days of the week (0 = saturday). Their corresponding
            values are the number of sundays that fall on the first
            of each month in that leap year.
        :param this.yearLookupIndex:
            The index into each yearLookup dictionary. The value
            of this variable corresponds to the first day in a year
            (0 = saturday).
        :param this.sizeOfWeek:
            A week has seven days.
        :param this.sundayCount:
            A counter of all sundays that fall on the first of a month
            between this.currentYear and this.endYear.
        :param this.curentYear:
            The current year.
        :param this.endYear:
            The year to end calculations on.
        :param this.quotient:
            The quotient of the number of years to iterate over divided
            by 28 (28 year cycle), multiplied by the number of
            Sundays that fall on the first of the months inside the 28
            year cycle (48). 
            '''

        this.yearLookup = {0: 1, 1: 2, 2: 2, 3: 2, 4: 1, 5: 3, 6: 1}
        this.leapYearLookup = {0: 1, 1: 3, 2: 2, 3: 1, 4: 2, 5: 2, 6: 1}
        this.yearLookupIndex = 3
        this.sizeOfWeek = 7
        this.sundayCount = 0
        this.currentYear = 1901
        this.endYear = 2001
        this.quotient = 0

    def calculateSundaysInYear(this) -> None:
        if this.checkLeapYear():
            this.sundayCount += this.leapYearLookup[this.yearLookupIndex]
            this.yearLookupIndex += 2
        else:
            this.sundayCount += this.yearLookup[this.yearLookupIndex]
            this.yearLookupIndex += 1

    def getQuotientResult(this):
        '''Updates the value this.quotient to the number of Sundays
        that fall on the first of each month in the 28 year cycles
        between the currentYear and endYear.'''
        numberOfYears = (this.endYear - this.currentYear)
        this.quotient = numberOfYears // 28
        this.currentYear += (this.quotient * 28)
        this.quotient *= 48


    def updateLookupIndex(this) -> None:
        '''If the lookup index, which corresponds to the days 
        of the week, exceeds the number of days in a week it wraps
        around the week again.'''
        this.yearLookupIndex %= this.sizeOfWeek


    def checkLeapYear(this) -> bool:
        return (this.currentYear % 4 == 0) and (this.currentYear % 100 != 0 or this.currentYear % 400 == 0)

    
    def incrementYear(this, step: int = 1) -> None:
        this.currentYear += step


    def calculateSolution(this):
        '''calculates all days that fall on the first of a month
        between this.currentYear and this.endYear'''

        this.getQuotientResult()

        while this.currentYear < this.endYear:

            this.calculateSundaysInYear()

            if this.yearLookupIndex >= this.sizeOfWeek:
                this.updateLookupIndex()

            this.incrementYear()

        return this.sundayCount + this.quotient


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateSolution()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))
