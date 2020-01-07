def leastFactorial(n):
    m = 0
    while math.factorial(m) <= n:
        if math.factorial(m) == n:
            break
        m+=1
    return math.factorial(m)
            