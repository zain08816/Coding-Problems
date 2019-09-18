def firstMultiple(d, s):
    a = True
    while True:
        a = True
        for i in d:
            if s % i != 0:
                a = False
        if a == True:
            return s
        s += 1
        