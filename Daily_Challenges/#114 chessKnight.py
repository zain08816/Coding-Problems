def chessKnight(cell):
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    c = 0
    for i in range(len(dx)):
        a = dx[i] + (ord(cell[0]) - ord('a'))
        b = dy[i] + (int(cell[1]) - 1)
        if 0 <= a < 8 and 0 <= b < 8:
            c += 1
    return c

