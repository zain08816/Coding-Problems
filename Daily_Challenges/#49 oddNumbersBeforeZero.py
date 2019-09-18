def oddNumbersBeforeZero(s):
    c = 0
    for i in s:
        if i==0:
            return c
        if i%2==1:
            c += 1
