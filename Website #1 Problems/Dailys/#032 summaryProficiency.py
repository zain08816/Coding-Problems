def summaryProficiency(a, n, m):
    t = []
    for i in range(len(a)+1):
        if len(t) == n:
            return sum(t)
        if a[i] >= m:
            t.append(a[i])
        print(t)