def isLucky(n):
    n = list(map(int, str(n)))
    return sum(n[len(n)//2:]) == sum(n[:len(n)//2])
