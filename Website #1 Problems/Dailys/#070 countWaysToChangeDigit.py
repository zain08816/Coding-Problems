def countWaysToChangeDigit(v):
    l = list(map(int, str(v)))
    t = 0
    for i in l:
        t += 9-i
    return t