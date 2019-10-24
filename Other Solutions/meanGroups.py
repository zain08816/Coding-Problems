def meanGroups(a):
    d = {}
    res = []
    for index, g in enumerate(a):
        m = sum(g)/len(g)
        if m in d:
            d[m].append(index)
        else:
            d[m] = [index]
        print(d)
    for i in d:
        res.append(d[i])
    return res