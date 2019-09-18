def longestDigitsPrefix(s):
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    prefix = ""
    for i in range(len(s)):
        if s[i] not in d:
            return prefix
        if s[i] in d:
            prefix = prefix + s[i]
    return prefix