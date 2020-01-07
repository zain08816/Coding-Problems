def isMonotonous(s):
    if len(s)==1:
        return True
    if s[0] == s[1]:
        return False
    if s[0] > s[1]:
        for i in range(len(s)-1):
            if s[i]>s[i+1]:
                continue
            else:
                return False
        return True
    if s[0] < s[1]:
        for i in range(len(s)-1):
            if s[i]<s[i+1]:
                continue
            else:
                return False
    return True