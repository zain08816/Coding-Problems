def whoseMove(l, win):
    if win:
        if l == 'white':
            return 'white'
        return 'black'
    else:
        if l == 'white':
            return 'black'
        return 'white'