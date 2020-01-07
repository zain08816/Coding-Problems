def sequenceElement(a, n):
    while (n % 4686) > 0:
        a.append(sum(a) % 10)
        del(a[0])
        n-=1
    return a[0]