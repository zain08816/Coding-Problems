def allLongestStrings(inputArray):
    longest = 0
    combined = []
    for string in inputArray:
        if len(string) > longest:
            longest = len(string)
    for string in inputArray:
        if len(string) == longest:
            combined.append(string)
    return combined