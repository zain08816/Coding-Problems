def higherVersion(ver1, ver2):
    ver1 = ver1.split('.')
    ver2 = ver2.split('.')
    for i in range(len(ver1)):
        v1 = int(ver1[i])
        v2 = int(ver2[i])
        
        print(v1, v2)
        
        if v1 == v2:
            continue
        if v1 > v2:
            return True
        if v2 > v1:
            return False
    return False
        