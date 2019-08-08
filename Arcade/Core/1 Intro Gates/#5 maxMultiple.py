def maxMultiple(divisor, bound):
    while bound%divisor != 0:
        bound -= 1
    return bound