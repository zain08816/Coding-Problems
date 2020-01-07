def checkSameElementExistence(arr1, arr2):
    d = set()
    for i in arr1:
        d.add(i)
    for i in arr2:
        if i in d:
            return True
    return False