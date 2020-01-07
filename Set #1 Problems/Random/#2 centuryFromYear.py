def centuryFromYear(year):
    if year%100 == 0:
        return year/100
    else:
        cent = int(year/100) + 1
        return cent