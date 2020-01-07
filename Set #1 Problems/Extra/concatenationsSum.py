def concatenationsSum(a):
    total = 0
    for i in range(len(a)):
        a[i] = str(a[i])
    for i in a:
        for j in a:
            total += int(i+j)
    return total
