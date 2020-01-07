def applesDistribution(a, b, r):
    res = 0
    for i in range(1, b+1):
        if a % i <= r:
            res += 1
    return res