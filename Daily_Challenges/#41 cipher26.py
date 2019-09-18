def cipher26(message):
    arr = []
    arr.append(message[0])
    for i in range(1, len(message)):
        s = ord(message[i])-ord(message[i-1])
        if(s<0):
            arr.append(chr(123-abs(s)))
        else:
            arr.append(chr(97+s))
    return ''.join(arr)
