def chessBoardCellColor(cell1, cell2):
    a, b = "ACEG", "1357" 
    c, d = "BDFH", "2468"
    
    return (cell1[0] in a and cell1[1] in b or cell1[0] in c and cell1[1] in d) == (cell2[0] in a and cell2[1] in b or cell2[0] in c and cell2[1] in d)