def firstDigit(s):
    n = string.digits
    for i in s:
        if i in n:
            return i
