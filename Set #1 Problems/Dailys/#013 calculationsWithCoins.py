def calculationsWithCoins(a, b, c):
    return len(list(set([a, b, c, a+b, a+c, b+c, a+b+c])))
    