def knapsackLight(v1, w1, v2, w2, m):
    if w1+w2 <= m:
        return v1+v2
    if w1 <= m and v1 > v2:
        return v1
    if w2 <= m:
        return v2
    elif w1 <= m:
        return v1
    return 0