def variableName(name):
    allowed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    for i in range(len(name)):
        if name[0] in "0123456789":
            return False
        if name[i] in allowed:
            continue
        else:
            return False
    return True