def arraySumAdjacentDifference(arr):
    out = 0
    for i in range(len(arr)):
        if i == 0:
            continue
        out += abs(arr[i-1] - arr[i])
    return out