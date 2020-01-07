def directionOfReading(n):
    original = len(n)
    longest = str(max(n))    
    for i in range(len(n)):
        n[i] = [int(x) for x in str(n[i])]
        while len(n[i]) < len(longest):
            if len(n[i])==0:
                break
            n[i].insert(0, 0)
        print(n)
    out = [[n[j][i] for j in range(len(n))] for i in range(len(n[0]))]
    out = [int("".join(str(x) for x in i)) for i in out]
    if len(out) != original:
        while len(out) < original:
            out.insert(0,0)
    return(out)
    