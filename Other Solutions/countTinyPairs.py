def countTinyPairs(a, b, k):
    res = 0
    for i in range(len(a)):
        x = int(str(a[i])+str(b[i]))
        if x < k:
            res += 1
    return res