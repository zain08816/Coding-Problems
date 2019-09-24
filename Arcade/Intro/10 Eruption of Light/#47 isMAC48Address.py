def isMAC48Address(hexa):
    key = string.hexdigits
    print(key)
    if len(hexa) != 17:
        return False
    try:
        hexa = hexa.split('-')
    except:
        return False
    print(hexa)
    for i in hexa:
        if len(i) != 2:
            return False
        if i[0] in key and i[1] in key:
            continue
        else:
            return False
            
    return True
        
    