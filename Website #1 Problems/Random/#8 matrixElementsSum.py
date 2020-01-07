def matrixElementsSum(matrix):
    sum = 0
    outer = len(matrix)
    inner = len(matrix[0])
    for outer_i in range(inner):
        for inner_i in range(outer):
            if matrix[inner_i][outer_i] != 0:
                sum += matrix[inner_i][outer_i]
            else: 
                break
    return sum
