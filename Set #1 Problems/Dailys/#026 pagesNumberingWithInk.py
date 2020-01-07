def pagesNumberingWithInk(c, n):
    while n >= 0:
        n -= len(str(c))
        c += 1
    return c - 2