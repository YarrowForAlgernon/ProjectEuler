from time import time_ns
from math import floor


def adjustDates(month, year):
    if month == 1 or month == 2:
        year -= 1
        month += 12
    return month, year

def dayToTextConversion(dayOfWeek):
    dayOfWeekDict = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
    return dayOfWeekDict[dayOfWeek]

    
def getDayOfWeek(day, month, year):

    (month, year) = adjustDates(month, year)
    monthCode = floor((13 * (month + 1)) / 5)
    dayOfWeek = day + monthCode + year + floor(year / 4) - floor(year / 100) + floor(year / 400)
    dayOfWeek %= 7
    dayOfWeekString = dayToTextConversion(dayOfWeek)
    return dayOfWeekString


def checkMonthCounterExceedsYear(month):
    return month > 12


def calculateDaysOnFirstOfMonth(startYear, endYear):
    '''calculates all days that fall on the first of a month.'''

    month = 1
    sundayCount = 0

    while startYear  < endYear:

        firstOfMonth = getDayOfWeek(1, month, startYear)    

        month += 1

        if checkMonthCounterExceedsYear(month):
            startYear += 1
            month = 1

        if firstOfMonth == "Sunday":
            sundayCount += 1

    return sundayCount


if __name__ == "__main__":

    startTime = time_ns()
    noOfDays = calculateDaysOnFirstOfMonth(1901, 2001)
    stopTime = time_ns()
    print(noOfDays, "\nTime Taken (ns): " + str(stopTime - startTime))

