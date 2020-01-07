def smallestNumber(n):
    if n == 1:
        return 0
    num = '1'
    for i in range(n-1):
        num = num + '0'
    return int(num)