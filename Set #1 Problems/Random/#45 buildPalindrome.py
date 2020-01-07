def buildPalindrome(st):
    s = list(st)
    e = ''
    while s != s[::-1]:
        e = e + (s.pop(0))
    return st + e[::-1]
    