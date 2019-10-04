def houseOfCats(l):
    if l==2:
        return [1]
    l = l/2
    out = []
    while l >= 0:
        out.append(l)
        l = l-2
    return sorted(out)