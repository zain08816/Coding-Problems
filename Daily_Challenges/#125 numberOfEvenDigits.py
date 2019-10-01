def numberOfEvenDigits(n):
    n = str(n)
    res = 0
    for i in n:
        if int(i)%2 == 0:
            res += 1
    return res