def maxDivisor(l, r, d):
    largest = 0
    for i in range(l, r):
        if i%d == 0:
            largest = i
    if largest == 0:
        return -1
    else:
        return largest
    