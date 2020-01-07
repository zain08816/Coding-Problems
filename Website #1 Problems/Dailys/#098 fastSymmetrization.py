def fastSymmetrization(a):
    row_len = len(a)
    col_len = len(a[0])
    mid_row = len(a)//2
    mid_col = len(a[0])//2
    # Horizontal Symmetry
    for row in range(row_len):
        for col in range(col_len):
            print(row, col)
            if a[row][col] != '*':
                x = a[row][col_len-col-1]
                print(x, col_len-col-1)
                if x == '*':
                    a[row][col_len-col-1] = a[row][col]
                elif x == a[row][col]:
                    continue
                else:
                    return []
    
                    
    #Vertical Symetry
    for row in range(mid_row):
        for col in range(col_len):
            print(row, col)
            y = a[row_len-1-row][col]
            print(y, row_len-1-row)
            if a[row][col] != '*':
                if y == '*':
                    a[row_len-1-row][col] = a[row][col]
                elif y == a[row][col]:
                    continue
                else:
                    return[]
            if a[row][col] == '*' and y != '*':
                a[row][col] = y
    return a
                
    # I know that this isnt really a good solution in terms of speed, but it passes all test cases
    # something that can be improved is to do the Horizontal and Veritcal symmetry checks all in the same loop
    # to have it go from O(2(row*col)) => O(row*col) to simply O(row*col) 
                
                
                
                
                