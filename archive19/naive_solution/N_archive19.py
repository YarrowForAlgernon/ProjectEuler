# 1 jan 1900 was monday.
'''Thirty days has September,
April, June and November. (4, 6, 11, 9)
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.'''
'''How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

def checkDaysExceedMonth(dayCount, daysInMonth):
    return dayCount > daysInMonth


def checkLeapYear(yearCount):
    if (yearCount % 4 == 0) and (yearCount % 100 != 0 or yearCount % 400 == 0):
        return True
    return False


def calculateSundays():

    # to create in one function a way to modulate theh day count and increase the month count.
    largeMonthDays = 31
    smallMonthDays = 30
    februaryDays = 28
    leapDays = 29
    daysInMonthList = [31, 30, 29, 28]
    smallMonthList = [4, 6, 9, 11]
    dayCount = 7 # will always point to sunday
    sundayCount = 0
    monthCount = 1 #jan
    yearCount = 1900

    while yearCount < 2001:
        
        if monthCount == 2:
            if checkLeapYear(yearCount):
                print("day: " + str(dayCount), "Leap Year: " + str(yearCount))
                if checkDaysExceedMonth(dayCount, leapDays):
                    dayCount %= leapDays
                    monthCount += 1
            elif checkDaysExceedMonth(dayCount, februaryDays):
                dayCount %= februaryDays
                monthCount += 1

        elif monthCount in smallMonthList:
            if checkDaysExceedMonth(dayCount, smallMonthDays):
                dayCount %= smallMonthDays
                monthCount += 1

        else:
            if checkDaysExceedMonth(dayCount, largeMonthDays):
                dayCount %= largeMonthDays
                monthCount += 1

        if monthCount == 13:
            yearCount += 1
            monthCount = 1

        if dayCount == 1:
            print("Month: " + str(monthCount), "Year: " + str(yearCount))
            sundayCount += 1

        print("day: " + str(dayCount), "month: " + str(monthCount), "year: " + str(yearCount))
        dayCount += 7

    return sundayCount-2


if __name__ == "__main__":
    print(checkLeapYear(2000), checkLeapYear(1976), checkLeapYear(1960))

    sundays = calculateSundays()
    print(sundays)

