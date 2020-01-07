def minimalMultiple(divisor, lowerBound):
    c = lowerBound
    
    while True:
        print(c)
        if c%divisor == 0:
            return c
        c += 1