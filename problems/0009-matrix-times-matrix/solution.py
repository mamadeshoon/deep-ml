def matrixmul(a: list[list[int | float]], b: list[list[int | float]]) -> list[list[int | float]]:
    m = len(a)
    n = len(a[0])
    p = len(b)
    q = len(b[0])

    if n != p:
        return -1

    c = [[0] * q for _ in range(m)]

    for i in range(m):
        for k in range(q):
            for j in range(n):
                c[i][k] += a[i][j] * b[j][k]

    return c