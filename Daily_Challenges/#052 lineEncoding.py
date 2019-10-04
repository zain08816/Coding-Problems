def lineEncoding(s):
    c = 0
    p = ''
    out = ''
    for l in s:
        if l == p:
            c += 1
            continue
        else:
            if c > 1:
                out += str(c)
            out += p
            c = 1
            p = l
    if c > 1:
        out += str(c)
    out += p
    return out