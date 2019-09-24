def spiralNumbers(n):
    out = [[0] * n for i in range(n)]
    p, d = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += p[i % 4]
            y += d[i % 4]
            out[x][y] = c
            c += 1
    return out