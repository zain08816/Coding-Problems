def isArithmeticProgression(s):
    l = s[0]-s[1]
    for i in range(len(s)-1):
        if s[i]-s[i+1] != l:
            return False
    return True