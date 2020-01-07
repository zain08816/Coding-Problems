def digitDegree(n):
    deg = 0
    while n>=10:
        n = sum([int(x) for x in str(n)])
        deg += 1
    return deg