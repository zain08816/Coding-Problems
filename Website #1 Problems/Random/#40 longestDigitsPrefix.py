def longestDigitsPrefix(s):
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    out = ''
    for i in s:
        if i not in d:
            return out
        if i in d:
            out += i
    return out
            