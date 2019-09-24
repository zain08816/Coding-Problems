def lineEncoding(s):
    result = ''
    i = 0
    while i < len(s):
        current_count = 1
        while i+1 < len(s) and s[i+1] == s[i]:
            current_count+=1
            i+=1
        if current_count > 1:
            result+= str(current_count)
        result+= s[i]
        i+=1
        print(i, result)
    return result
