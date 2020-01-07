def countTinyPairs(a, b, k):
    res = 0
    l = len(a)
    for i in range(l):
        x = int(str(a[i]) + str(b[l-i-1]))
        if x < k:
            res += 1
    return res