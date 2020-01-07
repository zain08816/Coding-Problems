def firstDigit(s):
    for i in s:
        try:
            int(i)
            return i
        except:
            continue