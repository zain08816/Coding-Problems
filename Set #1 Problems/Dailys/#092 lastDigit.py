def lastDigit(a, b):
    if b == 0:
        return 1
    
    if b%4 == 0:
        b = 4
        a %= 10
        res = math.pow(a,b)
        return res%10
    
    a = a%10
    b = b%4
    
    res = math.pow(a,b)
    print(res)
    
    return res%10
    
