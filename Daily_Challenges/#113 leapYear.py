import calendar
def leapYear(year):
    return calendar.isleap(year)

    # if year % 400 == 0:
    #     return True
    # if year % 100 == 0:
    #     return False
    # if year % 4 == 0:
    #     return True
    # else:
    #     return False