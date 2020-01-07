def tennisSet(score1, score2):
    hi = max(score1, score2)
    low = min(score1, score2)
    if hi <= 5:
        return False
    if hi > 7:
        return False
    if hi==7:
        if low == 5 or low == 6:
            return True
        else:
            return False
    if hi==6:
        if low < 5:
            return True
        else:
            return False