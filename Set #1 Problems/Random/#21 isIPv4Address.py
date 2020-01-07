def isIPv4Address(ip):
    split = ip.split('.')
    print(split)
    for i in split:
        try:
            print(int(i))
        except:
            return False
    if len(split) != 4:
        return False
    if len(split) == 4:
        return (int(split[0]) in range(256)) and (int(split[1]) in range(256)) and (int(split[2]) in range(256)) and (int(split[3]) in range(256))
        