def evenNumbersBeforeFixed(sequence, fixedElement):
    count = 0
    
    for i in sequence:
        if i == fixedElement:
            return count
        if i%2 == 0:
            count += 1
    return -1