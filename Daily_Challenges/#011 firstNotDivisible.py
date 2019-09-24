def firstNotDivisible(d, s):
    while True:
        div = False
        for i in d:
            if s%i==0:
                div = True       
        if div == False:
            return s
        s += 1