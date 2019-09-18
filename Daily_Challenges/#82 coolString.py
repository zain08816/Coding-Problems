def coolString(s):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    if s[-1] not in lower and s[-1] not in upper:
        return False
    for i in range(0, len(s)-1):
        if s[i] not in lower and s[i] not in upper:
            return False
        if s[i] in lower and s[i+1] in lower:
            return False
        if s[i] in upper and s[i+1] in upper:
            return False
    return True