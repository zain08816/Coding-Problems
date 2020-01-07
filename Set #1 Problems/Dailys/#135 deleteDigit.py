def deleteDigit(n):
    largest = 0
    n = str(n)
    for i in range(len(n)):
        temp = n
        temp = temp[:i] + temp[i+1:] 
        if int(temp) >= largest:
            largest = int(temp)
    return largest

