def checkFactorial(n):
    fac = 0
    while math.factorial(fac) <= n:
        if math.factorial(fac) == n:
            return True
        fac += 1
    return False