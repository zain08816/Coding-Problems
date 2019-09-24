def arrayReplace(arr, rep, sub):
    for i in range(len(arr)):
        if arr[i] == rep:
            arr[i] = sub
    return arr