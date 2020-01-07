def unusualLexOrder(w):
    for i in range(len(w)):
        w[i] = w[i][::-1]
    w.sort()
    for i in range(len(w)):
        w[i] = w[i][::-1]
    return w