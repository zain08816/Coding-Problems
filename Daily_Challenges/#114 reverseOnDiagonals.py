def reverseOnDiagonals(m):
    l = len(m)-1 

    mid = len(m)//2
    x = 0
    for i in range(mid):
        m[i][x], m[l-x][l-x] = m[l-x][l-x], m[i][x]
        
        m[i][l-x], m[l-x][i] = m[l-x][i], m[i][l-x]
        
        x += 1

            
    return m