def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for i in range(len(matrix)):
			m = 0
			for j in range(len(matrix[0])):
				m += matrix[i][j]
			means.append(m / len(matrix[0]))
	if mode == "column":
		for j in range(len(matrix[0])):
			m = 0
			for i in range(len(matrix)):
				m += matrix[i][j]
			means.append(m / len(matrix))
	
	return means