def evenDigitsOnly(n):
    n = list(map(int, str(n)))
    for i in n:
        if i%2 != 0:
            return False
    return True