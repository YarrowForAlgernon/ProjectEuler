from time import time_ns
from math import floor


class archive19:
    
    
    def getDayOfWeek(this, day = 1, month = 13):

        monthCode = floor((13 * (month + 1)) / 5)
        this.dayOfWeek = day + monthCode + (this.yearCount-1) + floor((this.yearCount-1) / 4) - floor((this.yearCount-1) / 100) + floor((this.yearCount-1) / 400)
        this.dayOfWeek %= 7


    def __init__(this): # 0 = saturday

        this.yearLookup = {0: 1, 1: 2, 2: 2, 3: 2, 4: 1, 5: 3, 6: 1, 7: 1, 8: 3, 9: 2, 10: 1, 11: 2, 12: 2, 13: 1}
        this.dayOfWeek = 0
        this.sundayCount = 0
        this.yearCount = 1900


    def checkLeapYear(this):
        if (this.yearCount % 4 == 0) and (this.yearCount % 100 != 0 or this.yearCount % 400 == 0):
            return True
        return False

    def incrementYear(this):
        this.yearCount += 1

    def incrementSundayCount(this):
        if this.checkLeapYear():
            this.dayOfWeek += 7
        this.sundayCount += this.yearLookup[this.dayOfWeek]


    def calculateSolution(this):
        '''calculates all days that fall on the first of a month.'''

        while this.yearCount < 2017:

            this.getDayOfWeek()

            this.incrementSundayCount()

            print("Year: " + str(this.yearCount), "dayOfWeek: " + str(this.dayOfWeek), "no of sundays: " + str(this.yearLookup[this.dayOfWeek]))

            this.incrementYear()

        return this.sundayCount


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateSolution()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))
