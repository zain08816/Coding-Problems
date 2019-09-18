def fibonacciNumber(n):
    f = [1, 1]
    if n <= 2:
        return 1
    for i in range(n-1):
        f.append(f[0]+f[1])
        f.pop(0)
        print(f)
    return f[0]