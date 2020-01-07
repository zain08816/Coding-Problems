def reflectString(inputString):
    d = {}
    s = string.ascii_lowercase
    res = ''
    for i in range(len(s)):
        d[s[i]] = s[len(s)-i-1]
    print(d)
    
    for i in inputString:
        res += d[i]
        
    return res
        