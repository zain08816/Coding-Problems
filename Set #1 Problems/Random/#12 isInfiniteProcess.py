def isInfiniteProcess(a, b):
    if a > b or abs(a-b)%2==1:
        return True
    else:
        return False
