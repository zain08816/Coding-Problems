def palindromeRearranging(s):
    m = {}
    odd = 0
    #adding items to map
    for i in range(len(s)):
        m[s[i]] = 0
    #counting number of repeated numbers
    for i in s:
        if i in m:
            m[i] += 1
    #checking number of odds        
    for v in m.values():
        if v%2 != 0:
            odd += 1
    #if there is one odd and the length is odd  
    print(m)  
    if odd == 1 and (len(s)%2!=0):
        return True
    elif odd==0 and (len(s)%2==0):
        return True
    else:
        return False
