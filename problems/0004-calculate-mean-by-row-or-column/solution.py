def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == "row":
        for i in range(len(matrix)):
            avg = 0
            for j in range(len(matrix[0])):
                avg += matrix[i][j]
            means.append((1/len(matrix))*avg)
    elif mode == "column":
        for i in range(len(matrix[0])):
            avg = 0
            for j in range(len(matrix)):
                avg += matrix[j][i]
            means.append((1/len(matrix))*avg)

	return means