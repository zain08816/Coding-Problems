def buildPalindrome(s):
    c = list(s)
    pre = ''
    if s == s[::-1]:
        return s
    while c != c[::-1]:
        pre += c.pop(0)
        print(pre)
    return s + pre[::-1]