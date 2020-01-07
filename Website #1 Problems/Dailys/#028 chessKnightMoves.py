def chessKnightMoves(c):
    return [2,3,4,6,8][sum(1 if x in 'bg27' else 2 for x in c if x not in 'ah18')]
