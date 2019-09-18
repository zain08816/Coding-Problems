def countSumOfTwoRepresentations2(n, l, r):
    o = 0
    k = {}
    for i in range(l, r+1):
        k[i] = 1
    
    for i in k.keys():
        try:
            if k[n - i] == 1:
                o += 1
        except:
            continue
            
    return math.ceil(o/2)