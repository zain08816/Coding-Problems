def differentDigitsNumberSearch(arr):
    for i in arr:
        l = list(str(i))
        d = {t : 0 for t in l}
        print(l, len(l))
        print(d, len(d))
        if len(l) == len(d):
            return i
    return -1