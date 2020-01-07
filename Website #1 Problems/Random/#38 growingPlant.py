def growingPlant(u, d, h):
    c = 0
    x = 0
    while x <= h:
        c +=1
        x += u
        if x >= h:
            return c
        x -= d
    return c