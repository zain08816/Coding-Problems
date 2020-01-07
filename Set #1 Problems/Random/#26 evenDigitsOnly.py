def evenDigitsOnly(n):
    arr = list(str(n))
    for i in range(len(arr)):
        if int(arr[i])%2 == 0:
            continue
        else:
            return False
    return True