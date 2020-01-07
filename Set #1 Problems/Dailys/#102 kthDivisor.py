def kthDivisor(n, k):
    d = [i for i in range(1, n+1) if n%i == 0]
    try:
        return d[k-1]
    except:
        return -1