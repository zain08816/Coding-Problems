def sortByHeight(a):
    sort = sorted([num for num in a if num != -1])
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sort.pop(0)
    return a