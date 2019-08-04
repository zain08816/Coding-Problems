def arrayChange(a):
    c = 0
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            dif = (a[i-1] - a[i])+1
            a[i] = a[i-1]+1
            c = c + dif
    return c