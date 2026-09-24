def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	m = len(matrix)
	n = len(matrix[0])
	b = [[0] * n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			b[i][j] = scalar * matrix[i][j]
	return b