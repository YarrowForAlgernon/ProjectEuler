

def convert(dayOfWeek):
    dayDict = {0: "Tu", 1: "W", 2: "Th", 3: "F", 4: "Sa", 5: "Su", 6: "M"}
    return dayDict[dayOfWeek]


def ZellersCong(day, month, year):
    
    if month <= 2 and month > 0:
        month += 12
        year -= 1

    monthCode = (13 * (month+1)) // 5
    yearOfCentury = year % 100
    J = year // 100
    dayOfWeek = day +  monthCode + yearOfCentury + (yearOfCentury // 4) + (J //4) -(2 * J)
    dayOfWeek %= 7
    return dayOfWeek

if __name__ == "__main__":
    date = ZellersCong(13, 8, 2025)
    print(date)
