def circleOfNumbers(n, firstNumber):
    half = n/2 
    if firstNumber >= half:
        return firstNumber - half
    else:
        return firstNumber + half