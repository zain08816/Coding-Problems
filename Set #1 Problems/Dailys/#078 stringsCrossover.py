def stringsCrossover(arr, result):
    wrong = 0
    pairs = []    

    #creating pairs
    for p1 in range(len(arr)):
        for p2 in range(p1+1, len(arr)):
            pairs.append((arr[p1], arr[p2]))
    
    for pair in pairs:
        t = True
        for i in range(len(pair[0])):
            if not (pair[1][i] == result[i] or pair[0][i] == result[i]):
                t = False
        if t == False:
            wrong += 1
                
    return len(pairs) - wrong