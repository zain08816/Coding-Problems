def swapDiagonals(m):
        ml = len(m)
        for y in range(ml):
                m[y][y], m[y][ml-y-1] = m[y][ml-y-1], m[y][y]
        return m