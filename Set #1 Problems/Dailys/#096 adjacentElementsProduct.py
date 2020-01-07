def adjacentElementsProduct(arr):
    largest = -99999
    for i in range(1, len(arr)):
        print(i)
        x = arr[i]*arr[i-1]
        if x > largest:
            largest = x
    return largest
