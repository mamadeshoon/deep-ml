def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	m = len(a)
	n = len(a[0])
	l = len(b)
	if n != l:
		return -1
	c = []
	for i in range(m):
		c_i = 0
		for j in range(n):
			c_i += a[i][j] * b[j]
		c.append(c_i)
	return c