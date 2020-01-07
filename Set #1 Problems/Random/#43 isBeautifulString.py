def isBeautifulString(s):
    print(string.ascii_lowercase)
    r = [s.count(i) for i in string.ascii_lowercase]
    print(r)
    
    return r[::-1] == sorted(r)

