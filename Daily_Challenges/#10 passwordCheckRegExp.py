def passwordCheckRegExp(S):
    low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    has_cap = False
    has_num = False
    has_low = False
    if len(S) < 5:
        return False
    
    for i in S:
        if i in cap:
            has_cap = True
        if i in low:
            has_low = True
        if i in num:
            has_num = True
    return has_cap and has_low and has_num