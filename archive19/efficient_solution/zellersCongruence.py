from time import time_ns

class archive19:


    def __init__(this):
        '''
        :param this.sundayCount:
            The number of Sundays that fall on the first of the 
            months between this.currentYear and this.endYear.
        :param this.month:
            The month used in calculation of Zellers congruence 
            (February = 14, March = 3).
        :param this.zellerYear:
            The year used in calculation of Zellers congruence, which
            is the previous year if the current month is January
            or February.
        :param this.currentYear:
            The current Year which we start calculations on.
        :param this.endYear:
            The year to end calculations on.
        :param this.firstOfMonth:
            An integer value between 0-6, which correspond to the
            days of the week (0 = >Saturday).
        :param this.day:
            The day to use in calculation of zellers congruence.
            '''

        this.sundayCount = 0
        this.month = 13
        this.zellerYear = 1900
        this.currentYear = 1901
        this.endYear = 2001
        this.firstOfMonth = 0
        this.day = 1


    def adjustDate(this) -> None:
        if this.month > 14:
            this.month = 3
            this.zellerYear += 1
        if this.month == 12:
            this.currentYear += 1


    def getFirstOfMonth(this) -> None:                                                                                                                          
        monthCode = (13 * (this.month + 1)) // 5
        this.firstOfMonth = this.day + monthCode + this.zellerYear + (this.zellerYear // 4) - (this.zellerYear // 100) + (this.zellerYear // 400)
        this.firstOfMonth %= 7


    def checkForFirstSunday(this) -> None:
        if this.firstOfMonth == 1:
            this.sundayCount += 1

    
    def incrementMonth(this, step: int = 1) -> None:
        this.month += step


    def calculateDaysOnFirstOfMonth(this) -> int:
        '''calculates all Sundays that fall on the first of a month
        between this.currentYear and this.endYear.'''

        while this.currentYear  < this.endYear:

            this.getFirstOfMonth()

            this.checkForFirstSunday()

            this.incrementMonth()

            this.adjustDate()

        return this.sundayCount


if __name__ == "__main__":

    startTime = time_ns()
    archiveSolution = archive19()
    noOfDays = archiveSolution.calculateDaysOnFirstOfMonth()
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))
