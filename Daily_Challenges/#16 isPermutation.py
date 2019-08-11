def isPermutation(n, inputArray):
    return [i for i in range(n+1)][1:] == sorted(inputArray)