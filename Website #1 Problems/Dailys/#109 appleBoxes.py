def appleBoxes(k):
    r = y = 0
    for i in range(1, k+1):
        if i%2 == 0:
            r += i**2
        else:
            y += i**2
    return r-y
