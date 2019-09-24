def fromDecimal(b, n):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
        
    out = [str(i) for i in digits[::-1]]
    return ''.join(out)
    