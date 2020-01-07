def decipher(cipher):
    res = ''
    while len(cipher) != 0:
        if cipher[0] == '9':
            res += chr(int(cipher[:2]))
            cipher = cipher[2:]
        else:
            res += chr(int(cipher[:3]))
            cipher = cipher[3:]
    return res