def firstReverseTry(arr):
    if arr == []:
        return []
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr