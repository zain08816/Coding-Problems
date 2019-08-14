def eulersTotientFunction(n):
    res = [1]
    for i in range(2, n):
        if math.gcd(n,i) == 1:
            res.append(i)
        print(res)
    return len(res)