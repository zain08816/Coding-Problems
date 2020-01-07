def isLucky(n):
    array = list(map(int, str(n)))
    half = len(array)//2
    first = 0
    second = 0
    for num in array[:half]:
        first += num
    for num in array[half:]:
        second += num
    if second == first:
        return True
    else: 
        return False