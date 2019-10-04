def comfortableNumbers(l, r):
    c = 0
    for a in range(l, r+1):
        sa = a + sum(map(int,str(a)))
        for b in range(a+1, min(r, sa)+1):
            if a >= b - sum(map(int,str(b))):
                c+=1
    return c
