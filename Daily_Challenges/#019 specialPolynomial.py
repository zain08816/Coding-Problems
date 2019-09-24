def specialPolynomial(x, n):
    out = 0
    c = 0
    while True:
        if out > n:
            return c-2
        out += x**c
        c += 1