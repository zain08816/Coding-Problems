def lateRide(n):
    minutes = n%60
    print(minutes)
    hours = int((n-minutes)/60)
    print(hours)
    total = 0
    Smin = str(minutes)
    print(Smin)
    Shour = str(hours)
    print(Shour)
    for i in range(len(Smin)):
        total += int(Smin[i])
    for i in range(len(Shour)):
        total += int(Shour[i])
    return total