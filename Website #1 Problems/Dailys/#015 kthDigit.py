def kthDigit(n, k):
    try:
        return int(str(n)[k-1])
    except:
        return -1