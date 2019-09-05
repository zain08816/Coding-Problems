def houseNumbersSum(arr):
    total = 0
    for i in arr:
        total += i
        if i == 0:
            return total