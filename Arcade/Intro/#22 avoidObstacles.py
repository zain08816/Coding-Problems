def avoidObstacles(inputArray):
    i=2
    while True:
        if all(x%i!=0 for x in inputArray):
            return i
        i=i+1
