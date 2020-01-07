def isOneSwapEnough(s):
    y = list(s)
    for i in range(len(s)):
        for p in range(len(s)):
            y[i], y[p] = y[p], y[i]
            if y == y[::-1]:
                return True
            else:
                y = list(s)
    return False