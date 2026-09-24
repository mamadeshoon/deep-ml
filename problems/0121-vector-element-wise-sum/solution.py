def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) != len(b):
		return -1
	r = []
	for i in range(len(a)):
		r.append(a[i] + b[i])
	return r