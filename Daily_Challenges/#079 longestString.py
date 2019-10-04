def longestString(a):
    maxi = 0
    for i in range(len(a)):
        if len(a[i]) >= len(a[maxi]):
            maxi = i
    return a[maxi]
    

