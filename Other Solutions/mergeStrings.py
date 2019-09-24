def mergeStrings(s1, s2):
    count1 = {}
    for i in s1:
        try:
            count1[i] += 1
        except:
            count1[i] = 1
    count2 = {}
    for i in s2:
        try:
            count2[i] += 1
        except:
            count2[i] = 1
            
    res = ''
    while True:
        if s1 == '':
            return res+s2
        if s2 == '':
            return res+s1
        
        if count1[s1[0]] == count2[s2[0]]:
            if s1[0] == s2[0]:
                res += s1[0]
                s1 = s1[1:]
            elif s1[0] < s2[0]:
                res += s1[0]
                s1 = s1[1:]
            else:
                res += s2[0]
                s2 = s2[1:]
            continue
        
        else:
            if count1[s1[0]] < count2[s2[0]]:
                res += s1[0]
                s1 = s1[1:]
            else:
                res += s2[0]
                s2 = s2[1:]
            continue
            
            
    return res