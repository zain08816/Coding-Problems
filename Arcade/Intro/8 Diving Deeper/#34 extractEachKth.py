def extractEachKth(i, k):
    return [i[x] for x in range(0, len(i)) if ((x+1)%k)!=0]