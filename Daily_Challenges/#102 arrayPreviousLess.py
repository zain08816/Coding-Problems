def arrayPreviousLess(items):
    res = []
    p = False
    for i, num in enumerate(items):
        p = True
        for j in items[:i][::-1]:
            if j < num:
                res.append(j)
                p = False
                break
        if p:
            res.append(-1)
    return(res)
                