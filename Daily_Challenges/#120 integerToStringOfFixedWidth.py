def integerToStringOfFixedWidth(n, w):
    n = str(n)
    ln = len(n)
    if ln == w:
        return n
    n = list(n)[::-1]
    
    if ln > w:
        while len(n) != w:
            n.pop()
        return ''.join(n)[::-1]
    else:
        while len(n) != w:
            n.append('0')
        return ''.join(n)[::-1]
    