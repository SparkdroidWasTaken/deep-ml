def matrixmul(a: list[list[int | float]], 
              b: list[list[int | float]]) -> list[list[int | float]]:
    if len(a[0]) != len(b):
        return -1

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum_product = 0
            for k in range(len(b)):
                sum_product += a[i][k] * b[k][j]
            row.append(sum_product)
        result.append(row)
    
    return result
