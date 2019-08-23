def parallelLines(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2, = line2
    if a1==0 or b1==0:
        if a2==0 or b2==0:
            return True
        else:
            return False
        
    return (a1/(-b1)) == (a2/(-b2))
