def bishopAndPawn(bishop, pawn):
    if (ord(bishop[0])+int(bishop[1])+ord(pawn[0])+int(pawn[1]))%2==0:
        if bishop[0] != pawn[0]:
            return True
        else:
            return False
    else:
        return False