def alphabeticShift(s):
    l=list(string.ascii_lowercase)
    return "".join('a' if i is 'z' else l[l.index(i)+1] for i in s)