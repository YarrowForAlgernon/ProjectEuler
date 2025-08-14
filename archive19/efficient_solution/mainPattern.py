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
            '''

        this.yearLookup = {0: 1, 1: 2, 2: 2, 3: 2, 4: 1, 5: 3, 6: 1}
        this.leapYearLookup = {0: 1, 1: 3, 2: 2, 3: 1, 4: 2, 5: 2, 6: 1}
        this.yearLookupIndex = 3
        this.sizeOfWeek = 7
        this.sundayCount = 0
        this.currentYear = 1901
        this.endYear = 2001


    def calculateSundaysInYear(this) -> None:
        if this.checkLeapYear():
            this.sundayCount += this.leapYearLookup[this.yearLookupIndex]
            this.yearLookupIndex += 2
        else:
            this.sundayCount += this.yearLookup[this.yearLookupIndex]
            this.yearLookupIndex += 1


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

        while this.currentYear < this.endYear:

            this.calculateSundaysInYear()

            if this.yearLookupIndex >= this.sizeOfWeek:
                this.updateLookupIndex()

            this.incrementYear()

        return this.sundayCount


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateSolution()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))
